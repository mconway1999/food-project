#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db
from models import User,Food,Recipe,SavedRecipe

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

with app.app_context():
    Food.query.delete()
    User.query.delete()
    SavedRecipe.query.delete()
    Recipe.query.delete()

user1= User(id=1,first_name='Maddy',last_name='Conway',type='admin')
user2= User(id=2,first_name='Dylan', last_name='Agosto',type='customer')

food1 = Food(id=1, food_category ='bread', food_type = 'multigrain', image='/images/Multigrain.png')
food2 = Food(id=2, food_category ='bread', food_type = 'white', image='/images/White.png')
food3 = Food(id=3, food_category ='bread', food_type = 'bun', image='/images/Bun.png')
food4 = Food(id=4, food_category ='bread', food_type = 'crossaint', image='/images/Crossaint.png')
food5 = Food(id=5, food_category ='bread', food_type = 'wheat', image='/images/Wheat.png')
food6 = Food(id=6, food_category ='bread', food_type = 'cinnamonraisin', image='/images/CinnamonRasin.png')
food7 = Food(id=7, food_category ='bread', food_type = 'lettucewrap', image='/images/LettuceWrap.png')
food8 = Food(id=8, food_category ='bread', food_type = 'collardwrap', image='/images/CollardWrap.png')
food9 = Food(id=9, food_category ='bread', food_type = 'nobread', image='/images/NoBread.png')
food10 = Food(id=10, food_category ='bread', food_type = 'rye', image='/images/Rye.png')
food11 = Food(id=11, food_category ='bread', food_type = 'pumpernickel', image='/images/Pumpernickel.png')
food12 = Food(id=12, food_category ='bread', food_type = 'sourdough', image='/images/Sourdough.png')
food13 = Food(id=13, food_category ='bread', food_type = 'potato', image='/images/Potato.png')
food14 = Food(id=14, food_category ='bread', food_type = 'pita', image='/images/Pita.png')
food15 = Food(id=15, food_category ='bread', food_type = 'ramen', image='/images/Ramen.png')

food16 = Food(id=16, food_category ='topping', food_type = '', image= '')
food17 = Food(id=17, food_category ='topping', food_type = '', image= '')
food18 = Food(id=18, food_category ='topping', food_type = '', image= '')
food19 = Food(id=19, food_category ='topping', food_type = '', image= '')
food20 = Food(id=20, food_category ='topping', food_type = '', image= '')
food21 = Food(id=21, food_category ='topping', food_type = '', image= '')
food22 = Food(id=22, food_category ='topping', food_type = '', image= '')
food23 = Food(id=23, food_category ='topping', food_type = '', image= '')
food24 = Food(id=24, food_category ='topping', food_type = '', image= '')
food25 = Food(id=25, food_category ='topping', food_type = '', image= '')
food26 = Food(id=26, food_category ='topping', food_type = '', image= '')
food27 = Food(id=27, food_category ='topping', food_type = '', image= '')
food28 = Food(id=28, food_category ='topping', food_type = '', image= '')
food29 = Food(id=29, food_category ='topping', food_type = '', image= '')
food30 = Food(id=30, food_category ='topping', food_type = '', image= '')
food31 = Food(id=31, food_category ='topping', food_type = '', image= '')
food32 = Food(id=32, food_category ='topping', food_type = '', image= '')
food33 = Food(id=33, food_category ='topping', food_type = '', image= '')
food34 = Food(id=34, food_category ='topping', food_type = '', image= '')
food35 = Food(id=35, food_category ='topping', food_type = '', image= '')
food36 = Food(id=36, food_category ='topping', food_type = '', image= '')
food37 = Food(id=37, food_category ='topping', food_type = '', image= '')
food38 = Food(id=38, food_category ='topping', food_type = '', image= '')
food39 = Food(id=39, food_category ='topping', food_type = '', image= '')
food40 = Food(id=40, food_category ='topping', food_type = '', image= '')
food41 = Food(id=41, food_category ='topping', food_type = '', image= '')
food42 = Food(id=42, food_category ='topping', food_type = '', image= '')
food43 = Food(id=43, food_category ='topping', food_type = '', image= '')
food44 = Food(id=44, food_category ='topping', food_type = '', image= '')
food45 = Food(id=45, food_category ='topping', food_type = '', image= '')




db.session.add_all(user1,user2)
db.session.commit()