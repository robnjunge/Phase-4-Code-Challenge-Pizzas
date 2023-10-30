from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant')

    def to_dict(self):
        pizza_list = []
        for rp in self.restaurant_pizzas:
            pizza_list.append({
                'id': rp.pizza.id,
                'name': rp.pizza.name,
                'ingredients': rp.pizza.ingredients
            })
        
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'pizzas': pizza_list
        }


    def __repr__(self):
        return f'<Restaurant {self.name}, ${self.address}>'

# add any models you may need. 

class Pizza(db.Model):

    __tablename__ = 'pizzas'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='pizza')

    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    def to_dict(self):
        d ={
        'id': self.id,
        'name': self.name,
        'ingredients': self.ingredients
        }
        return d
    
    def __repr__(self):
        return f'<Pizza {self.name}, ${self.ingredients}>'

class RestaurantPizza(db.Model):

    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Integer)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))

    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())

    def __repr__(self):
        return f'<RestaurantPizza {self.price}>'
