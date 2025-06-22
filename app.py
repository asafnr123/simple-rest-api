from flask import Flask, jsonify, request
from datetime import datetime
import uuid
from car import Car

app = Flask(__name__)
cars = {
    str(uuid.uuid4()): {"manufacturer": "Toyota", "model": "Corolla", "year": 2020, "hp": 150},
    str(uuid.uuid4()): {"manufacturer": "Honda", "model": "Civic", "year": 2021, "hp": 160}
}


@app.route("/", methods=['GET'])
def getHomePage():
    return "<h2>I love cars</h2>"



# get all cars:
@app.route("/cars", methods=['GET'])
def get_all_cars():

    if cars:
        return jsonify(cars), 200
    else:
        return jsonify({"error": "No cars found"}), 404
    



# create a car
@app.route("/cars", methods=['POST'])
def add_new_car():
    car = request.get_json()

    isCar, errorMsg = check_car_format(car) #returns a tuple of (true/flase, errorMsg)

    if isCar:
        try:
            newCar = Car(
                id= str(uuid.uuid4()),
                manufacturer= car["manufacturer"],
                model= car["model"],
                year= car["year"],
                horsePower= car["horsePower"]
            )

            cars[newCar.id] = newCar.to_json_format()
            return jsonify({"message": "Successfully Created", "car": newCar.to_json_format()}), 200
        
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    else:
        return jsonify({"error": errorMsg}), 400
        


    
    


    

# get a specific car
@app.route("/cars/<car_id>", methods=['GET'])
def get_car(car_id):
    car = cars.get(car_id)
    if car:
        return jsonify(cars[car_id]), 200
    else:
        return jsonify({"error": f"No car with id {car_id}"}), 404
    





# update a car
@app.route("/cars/<car_id>", methods=['PUT'])
def update_car(car_id):
    car = cars.get(car_id)

    if car:
        new_car = request.get_json()

        isCarType, errorMsg = check_car_format(new_car)

        if isCarType:
            cars[car_id] = new_car
            return jsonify({"message": f"Successfully updated {new_car['manufacturer']} {new_car['model']}"}), 200
        else:
            return jsonify({"error": f"ERROR: {errorMsg}"}), 400
    else:
        return jsonify({"error": f"No car with id {car_id}"}), 404


# delete a car
@app.route("/cars/<car_id>", methods=['DELETE'])
def remove_car(car_id):
    car = cars.get(car_id)

    if car:
        del cars[car_id]
        return jsonify({"message": f"Successfully deleted {car['manufacturer']} {car['model']}"}), 200
    else:
        return jsonify({"error": f"No car with id {car_id}"}), 404





# checks if a json request is a valid Car object, return true if all god, if not returns a tuple (false, error msg)
def check_car_format(json_car):
    
    required_fields = ["manufacturer", "model", "year", "horsePower"]

    # first check if car is a valid json
    if json_car is None:
        return False, "Invalid JSON format"
    # then check if json got all the required fields
    if all(field in json_car for field in required_fields):

        # check if the car's year is from 1885 until today, if its not return false
        if not (isinstance(json_car["year"], int) and 1885 <= json_car["year"] <= datetime.now().year ):
            return False, "Year must be a number between 1885 and current year"
        
        # check if the horse power is a number thats bigger then 0
        if not (isinstance(json_car["horsePower"], int) and json_car["horsePower"] > 0):
            return False, "Horse power must be a positive integer"
    else:
        return False, "Car must include the following parameters: manufacturer, model, year, horsePower" 
    
    return True, None
    
    
    
                
       
        
    
    



if __name__ == ("__main__"):
    app.run()