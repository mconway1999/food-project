#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
import requests

url= 'https://api.spoonacular.com/recipes/complexSearch'

response = requests.get(url)

if response.status_code == 200:
    print("Request successful!")
   
    data = response.json()  
    print(data)
else:
    print(f"Error: {response.status_code}")


# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

