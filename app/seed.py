from faker import Faker
from random import randint, choice as rc


from app import app
from models import db, Pizza, Restaurant, RestaurantPizza

fake = Faker()

with app.app_context():

    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    restaurant = []
    for i in range(20):
        rest = Restaurant(
            name = fake.name(),
            address = fake.address()
        )
        restaurant.append(rest)

        db.session.add_all(restaurant)
        db.session.commit()

    pizza = []
    for i in range(20):
        p = Pizza(
            name = fake.name(),
            ingredients = fake.word(),
        )
        pizza.append(p)

        db.session.add_all(pizza)
        db.session.commit()

    restaurant_pizza = []
    for i in range(20):
        rp = RestaurantPizza(
            price = randint(1, 30),
            pizza = rc(pizza),
            restaurant = rc(restaurant)

        )
        restaurant_pizza.append(rp)

        db.session.add_all(restaurant_pizza)
        db.session.commit()




