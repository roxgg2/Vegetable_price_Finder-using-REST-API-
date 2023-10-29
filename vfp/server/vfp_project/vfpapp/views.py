from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

fruits_and_vegetables = {
    "apple": 2.0,
    "banana": 2.6,
    "kiwi": 6.0,
    "carrot": 1.0,
    "tomato": 2.5,
    "eggplant": 3.0,
    "strawberry": 2.2,
    "grape": 2.8,
    "cucumber": 1.2,
    "orange": 1.5,
    "broccoli": 1.8,
    "lettuce": 1.0,
    "watermelon": 3.5,
    "peach": 2.3,
    "pepper": 1.4,
    "mango": 2.7,
    "spinach": 1.2,
    "pineapple": 3.2,
    "zucchini": 1.1,
    "pear": 2.4,
    "avocado": 2.9,
    "sweet potato": 1.6,
    "blueberry": 2.1,
    "cabbage": 1.3,
    "grapefruit": 1.7,
    "asparagus": 1.3,
    "raspberry": 2.0,
    "cauliflower": 1.4,
    "plum": 2.2,
    "pumpkin": 2.0,
}

# Convert the dictionary into a list of key-value pairs
fruits_and_vegetables_list = [{"name": name, "price": price} for name, price in fruits_and_vegetables.items()]

@api_view(["GET"])
def home(request):
    fruit_name = request.query_params.get('name', '').lower()

    if fruit_name in fruits_and_vegetables:
        fruit_price = fruits_and_vegetables[fruit_name]
        msg = f"The price of {fruit_name} is ${fruit_price:.2f}"
    else:
        msg = f"{fruit_name} not found in the database."
        return Response(fruits_and_vegetables_list)

    return Response({"msg": msg})
