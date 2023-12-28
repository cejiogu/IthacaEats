from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Assocation table relating Restaurant table to User table
rest_user_association = db.Table("rest_user_association", db.Model.metadata,
                                  db.Column("rest_id", db.Integer, db.ForeignKey("restaurants.id")),
                                  db.Column("user_id", db.Integer, db.ForeignKey("users.id")))


class Restaurant(db.Model):
    """
    Restaurant Model
    """
    __tablename__ = "restaurants"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # Do we need to include "nullable=False" in this line?
    name = db.Column(db.String, nullable=False)
    desc = db.Column(db.String, nullable=False) # TODO: Limit character size of description
    labels = db.Column(db.String, nullable=False)

    users = db.relationship("User", secondary=rest_user_association, back_populates="users")
    
    # Many-to-One relationship with 'Reviews' table (a Restaurant can have many Reviews, but a Review can only be associated with one Restaurant)
    # "Cascade='delete'": If a restaurant is removed, all of its associated reviews are deleted
    reviews = db.relationship("Review", cascade="delete")

    def __init__(self, **kwargs):
        """
        Initialize a Restaurant Object
        """
        self.name = kwargs.get("name")
        self.desc = kwargs.get("desc")
        self.labels = kwargs.get("labels")  #FIXME: Must be able to parse string in search of a specific label

    def serialize(self):
        """
        Serialize a Restaurant Object
        """
        return {
            "id": self.id,
            "name": self.name,
            "desc": self.desc,
            "labels": self.labels,
            "reviews": [r.serialize for r in self.reviews]
        }

class User(db.Model):
    """
    User Model
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    identifier = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    # Establish Many-to-Many relationship with 'Restaurants' table (many Users can be associated with many restaurants, and vice versa)
    restaurants = db.relationship("Restaurant", secondary=rest_user_association, back_populates="restaurants")

    # One-to-Many Relationship with 'Reviews' table (a User can be associated with many Reviews, but each Review may only be associated with one User)
    # "Cascade='delete'": If the User is deleted, all Reviews associated with the User are deleted  
    reviews = db.relationship("Review", cascade="delete")

    def __init__(self, **kwargs):
        """
        Initialize a User Object
        """
        self.f_name = kwargs.get("first_name")
        self.l_name = kwargs.get("last_name")
        self.username = kwargs.get("username")
        self.email = kwargs.get("email")
        self.password = kwargs.get("password")

    def serialize(self):
        """
        Serialize a User Object
        """
        return {
            "id": self.id,
            "first_name": self.f_name,
            "last_name": self.l_name,
            "username": self.username,
            "email": self.email,
            "reviews": [r.serialize() for r in Review.query.filter_by(user_id=self.id).all()]
        }

    def simple_serialize(self):
        """
        Serialize a User Object, providing less information for security purposes
        """
        return {
            "id": self.id,
            "username": self.username
        }
    
class Review(db.Model):
    """
    Review Model
    """
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rating = db.Column(db.Integer, nullable=False)
    desc = db.Column(db.String, nullable=False) # Reviewers should be forced to give detailed responses explaining their review
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    rest_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))

    user = db.relationship("User")

    def __init__(self, **kwargs):
        """
        Initialize Review Object
        """
        self.rating = f'{kwargs.get("rating")}/5'
        self.desc = kwargs.get("description")
    
    def serialize(self):
        """
        Serialize a Review Object
        """
        return {
            "id": self.id,
            "rest_id": Restaurant.query.filter_by(id=self.rest_id).first().serialize(),
            "rating": self.rating,
            "desc": self.desc,
            "user": User.query.filter_by(id=self.user_id).first().simple_serialize()
        }