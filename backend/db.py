from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    """
    Restaurant Model
    """
    __tablename__ = "restaurants"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # Do we need to include "nullable=False" in this line?
    name = db.Column(db.String, nullable=False)
    desc = db.Column(db.String, nullable=False) # TODO: Limit character size of description

    def __init__(self, **kwargs):
        """
        Initialize a Restaurant Object
        """
        self.name = kwargs.get("name")
        self.desc = kwargs.get("desc")

class User(db.Model):
    """
    User Model
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    identifier = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, **kwargs):
        """
        Initialize a User Object
        """
        self.identifier = kwargs.get("identifier")
        self.password = kwargs.get("password")