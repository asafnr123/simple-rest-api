
class Car:

    def __init__(self, car_id, manufacturer, model, year, horsePower):
        
        self.id = car_id
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.hp = horsePower


    
    def to_json_format(self):

        return {
            "id": self.id,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "year": self.year,
            "hp": self.hp
        }
    

    