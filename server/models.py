from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db

# Models go here!
class User(db.Model, SerializerMixin):
    __tablename__ ='users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)
    type = db.Column(db.String, nullable = False)

    @validates('first_name', 'last_name')
    def validate_name(self, attr, value):
        if (not isinstance(value, str)):
            raise ValueError(f"{attr} must be a string")
        return value
    
    @validates('type')
    def validate_type(self, column, value):
        if type(value) == str and (value == 'customer' or value == 'admin'):
            return value
        else:
            raise ValueError


class Recipe(db.Model, SerializerMixin):
    __tablename__='recipes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    ingredidents = db.Column(db.String, nullable=False)
    cook_time =db.Column(db.Integer, nullable=False)
    image = db.Column(db.String)
    description = db.Column(db.String, nullable=False)

class Food (db.Model, SerializerMixin):
    __tablename__='food'
    id = db.Column(db.Integer, primary_key=True)
    food_category = db.Column(db.String, nullable=False)
    food_type = db.Column(db.String, nullable=False)
    image = db.Column(db.String)

class SavedRecipe (db.Model, SerializerMixin):
    __tablename__='saved_recipes'
    id = db.Column(db.Integer, primary_key=True)

    user = db.relationship('User', back_populates='saved_recipes')
    recipe = db.relationship('Recipe', back_populates='saved_recipes')
    food = db.relationship('Food', back_populates='saved_recipes')
    