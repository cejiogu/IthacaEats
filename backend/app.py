import json
from db import Restaurant
from db import User
from db import Review
from flask import request
from db import db
from flask import Flask
import os

# Initialization of Application
app = Flask(__name__)
db_filename = "stores.db" # TODO: Come back to, change name

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_filename}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()


# Generalized Responses
def success_response(data, code=200):
    return json.dumps(data), code

def failure_response(message, code=404):
    return json.dumps({"error": message}), code

# List representing all possible labels that a restaurnt could use
labels = ["Vegan", "Thai", "Jamaican", "Korean", "Chinese", "Japanese", "Vietnamese", "LGBT+"]

# Routes - Restaurant Routes
# GET: Get all restaurants
@app.route("/")
@app.route("/<int:user_id>/restaurants/")
def base():
    """
    Endpoint that returns all restaurants and their informations
    """
    restaurants = [r.serialize() for r in Restaurant.query.all()]
    return success_response({"restaurants": restaurants})


# GET: Get information about a specific restaurant
@app.route("/<int:user_id>/restaurants/<int:rest_id>/")
def get_rest(rest_id):
    """
    Endpoint that returns the specific restaurant with restaurant id 'rest_id'
    """
    restaurant = Restaurant.query.filter_by(id=rest_id).first()
    if restaurant is None: # If the restaurant does not exist
        return failure_response("Restaurant not found!")
    return success_response(restaurant.serialize())


# GET: Get information about all restaurants that fall under a specific label "label"
@app.route("/user_id/restaurants/<string:label>/")
def get_spec_rest(label):
    pass


# POST: Create a Restaurant object and insert it into the database
@app.route("/restaurants/", methods=["POST"])
def create_restaurant():
    body = json.loads(request.data)
    name = body.get("name")
    if name is None:
        return failure_response("You did not enter the name of the restaurant!", 400)
    
    description = body.get("description")
    if description is None:
        return failure_response("You did not enter the description of the restaurant", 400)
    
    rest_labels = body.get("labels")
    if rest_labels is None:
        return failure_response("You did not enter any labels for the restaurant!", 400)
    
    restaurant = Restaurant(
        name=name,
        desc=description,
        labels=rest_labels
    )
    
    db.session.add(restaurant)
    db.session.commit()
    return success_response(restaurant.serialize(), 201)


# DELETE: Remove a specific Restaurant object with id "rest_id" from the database
@app.route("/restaurants/", methods=["DELETE"])
def delete_restaurant(rest_id):
    pass


# User Routes
# POST: Create a User
# TODO: Come back to, implement session tokens and password hashing
@app.route("/user/register/", methods=["POST"])
def register_user():
    """
    Endpoint that inserts a new User object into the database
    """
    body = json.loads(request.data)
    f_name = body.get("first_name")
    if f_name is None:
        return failure_response("You did not enter a first name!", 400)
    
    l_name = body.get("last_name")
    if l_name is None:
        return failure_response("You did not enter a last name!", 400)
    
    u_name = body.get("user_name")
    if u_name is None:
        return failure_response("You did not enter a user name!", 400)
    
    email = body.get("email")
    if email is None:
        return failure_response("You did not enter an email!", 400)
    
    password = body.get("password")
    if password is None:
        return failure_response("You did not enter a password!", 400)
    
    new_user = User(
        first_name=f_name,
        last_name=l_name,
        user_name=u_name,
        email=email,
        password=password
    )
    
    db.session.add(new_user)
    db.session.commit()
    return success_response(new_user.simple_serialize, 201)

# POST: Verifies whether the user currently exists or not
@app.route("/user/login/", methods=["POST"]) # TODO: Come back to, implement refresh session token 
def login():
    pass


# GET: Get a specific user with id "user_id"
@app.route("/users/<int:user_id>")
def get_user(user_id):
    user = User.query.filter_by(id=user_id)
    if user is None:
        return failure_response("User not found!")
    return success_response(user.serialize())


# POST: Create a review from a specific User for a specific Restaurant
@app.route("/user/<int:user_id>/restaurants/<int:rest_id>/")
def create_review(user_id, rest_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return failure_response("User not found!")
    
    restaurant = Restaurant.query.filter_by(id=rest_id).first()
    if restaurant is None:
        return failure_response("Restaurant not found!")

    body = json.loads(request.data)

    rating = body.get("rating")
    if rating is None:
        return failure_response("You did not enter a rating!", 400)
    
    description = body.get("description")
    if description is None:
        return failure_response("You did not enter a description!", 400)
    
    review = Review(
        rating=rating,
        desc=description,
        user_id=user_id,
        rest_id=rest_id
    )

    db.session.add(review)
    db.commit()
    return success_response(review.serialize(), 201)
    
