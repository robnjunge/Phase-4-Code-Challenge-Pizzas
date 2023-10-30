#!/usr/bin/env python3

from flask import Flask, make_response,jsonify,request
from flask_migrate import Migrate
from models import db, Restaurant, Pizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>HOME PAGE</h1>'

@app.route('/restaurants')
def restaurants():
    restaurant = Restaurant.query.all()
    data_format = [rest.to_dict() for rest in restaurant]

    response = make_response(
        jsonify(data_format),
        200
    )
    return response

@app.route('/restaurants/<int:id>', methods=['GET', 'DELETE'])
def restaurants_by_id(id):
    if request.method == 'GET':
        restaurant = Restaurant.query.filter_by(id=id).first()
        rest_dict = restaurant.to_dict()

        response = make_response(
            jsonify(rest_dict),
            200
        )
        return response
    
    elif request.method == 'DELETE':
        restaurant = Restaurant.query.filter_by(id=id).first()
        db.session.delete(restaurant)
        db.session.commit()
        restaurant_resp = {
            'Delete_Successful': True,
            'message': 'Restaurant Successfully deleted!'
        }
        response = make_response(
            jsonify(restaurant_resp), 200
        )
        return response

@app.route('/pizzas')
def pizzas():
    pizza = Pizza.query.all()
    data_format = [p.to_dict() for p in pizza]

    response = make_response(
        jsonify(data_format),
        200
    )
    return response




if __name__ == '__main__':
    app.run(port=5555)