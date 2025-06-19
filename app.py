from flask import FLask, jsonify, request

app = Flask(__name__)

cars = {
    1: {"manufacturer": "Toyota", "model": "Corolla", "year": 2020, "hp": 150},
    2: {"manufacturer": "Honda", "model": "Civic", "year": 2021, "hp": 160}
}



# get all cars:
@app.route("/cars", methods=['GET'])
def get_all_cars():
    None
    



# create a car


# get a specific car


# update a car



# delete a car