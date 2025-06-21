
class Car:

    def __init__(self, id, manufacturer, model, year, horsePower):
        
        self.id = id
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.horsePower = horsePower


    
    def to_json_format(self):

        return {
            "id": self.id,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "year": self.year,
            "horsePower": self.horsePower
        }
    

    