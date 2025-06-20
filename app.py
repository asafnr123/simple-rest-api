from flask import Flask, jsonify, request
import uuid
from car import Car

app = Flask(__name__)
cars = {
    str(uuid.uuid4()): {"manufacturer": "Toyota", "model": "Corolla", "year": 2020, "hp": 150},
    str(uuid.uuid4()): {"manufacturer": "Honda", "model": "Civic", "year": 2021, "hp": 160}
}


@app.route("/", methods=['GET'])
def getHomePage():
    return "<p>I love cars</p>"



# get all cars:
@app.route("/cars", methods=['GET'])
def get_all_cars():

    if cars:
        return jsonify(cars), 200
    else:
        return jsonify({"message": "No cars found"}), 404
    



# create a car
@app.route("/cars", methods=['POST'])
def add_new_car():
    required_fields = ["manufacturer", "model", "year", "horsePower"]
    car = request.get_json()

    if not all(field in car for field in required_fields):
        return jsonify({"error": "Invalid car data type"}), 400
    
    
    try:
        new_car = Car(
            car_id = str(uuid.uuid4()),
            manufacturer = car["manufacturer"],
            model = car["model"],
            year = car["year"],
            horsePower = car["horsePower"]
        )
    except TypeError:
        return jsonify({"error": "Invalid car data type"}), 400
    
    cars[new_car.id] = new_car.to_json_format()

    return jsonify({"id": new_car.id, "car": new_car.to_json_format()}), 201
    

# get a specific car
@app.route("/cars/<car_id>", methods=['GET'])
def get_car(car_id):
    car = cars.get(car_id)
    if car:
        return jsonify(cars[car_id])
    else:
        return jsonify({"message": f"No car with id {car_id}"}), 404




# update a car
@app.route("/cars/<car_id>", methods=['PUT'])
def update_car(car_id, new_car):
    car = cars.get(car_id)

    if car:
        if not all()


# delete a car




# a function that checks if a json request is a valid Car object

def check_car_format(car):
    required_fields = ["manufacturer", "model", "year", "horsePower"]

    



if __name__ == ("__main__"):
    app.run()