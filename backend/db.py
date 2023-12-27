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
            "users": [u.simple_serialize() for u in self.users]
        }

class User(db.Model):
    """
    User Model
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    identifier = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    restaurants = db.relationship("Restaurant", secondary=rest_user_association, back_populates="users")

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
            "email": self.email
        }

    def simple_serialize(self):
        """
        Serialize a User Object, providing less information for security purposes
        """
        return {
            "id": self.id,
            "username": self.username
        }