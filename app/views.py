from flask import Flask, render_template, url_for, request
from app import app

import requests, json

restaurants = [
    {
        'id': 1,
        'name': '1990 Vegan living',
        'address': 'Krossener Str. 19, 10245 Berlin',
        'food_type': 'vegan',
        'google_reviews': 4.6,
        'foodora_delivery': True
    }
]

@app.route('/')
def index():
	heading = "PyLadies Berlin"
	subheading = "You are welcome"
	foods = ['pasta','pizza','salad','dessert']
	return render_template('index.html', heading=heading, subheading=subheading, foods=foods)

@app.route('/restaurants')
def get_restaurants():
	heading = "restaurants"
	subheading = "A selection of the best places to eat locally"
	return render_template('restaurants.html', heading=heading, subheading=subheading, restaurants=restaurants)

@app.route('/randomusers')
def randos():
    heading = "API's"
    subheading = "Accessing the Random User API"
    url = "https://randomuser.me/api/?results=50"
    response = requests.request("GET", url)
    return render_template('randomusers.html', heading=heading, subheading=subheading, people=response.json())
