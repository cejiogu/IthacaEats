import json
from db import Restaurant
from db import User
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


# Routes - Restaurant Routes
# GET: Get information about all restaurants
@app.route("/")
@app.route("/restaurants/")
def base():
    pass


# GET: Get information about a specific restaurant with id "rest_id"
@app.route("/restaurants/<int:rest_id>/")
def get_rest(rest_id):
    pass


# GET: Get information about all restaurants that fall under a specific label "label"
@app.route("/restaurants/<string:label>/")
def get_spec_rest(label):
    pass


# GET: Get all reviews for a specific restaurant with id "rest_id"
@app.route("/restaurants/<int:rest_id>/reviews/")
def get_rest_reviews(rest_id):
    pass


# POST: Create a Restaurant object and insert it into the database
@app.route("/restaurants/", methods=["POST"])
def create_restaurant():
    pass


# DELETE: Remove a specific Restaurant object with id "rest_id" from the database
@app.route("/restaurants/", methods=["DELETE"])
def delete_restaurant(rest_id):
    pass


# User Routes
# POST: Create a User object and insert it into the database
@app.route("/user/register/", methods=["POST"])
def register_user():
    pass

# POST: Verifies whether the user currently exists or not
@app.route("/user/login/", methods=["POST"]) # TODO: Come back to, implement refresh session token 
def login():
    pass


# GET: Get a specific user with id "user_id"
@app.route("/users/<int:user_id>")
def get_user(user_id):
    pass


# POST: Create a review from a specific User for a specific Restaurant
@app.route("user/<int:user_id>/restaurants")
def create_review():
    pass