class Vehicle:
    def __init__(self, make, model):
        self.make = make 
        self.model = model 
        
    def get_info(self):
        return f"Vehicle: {self.make}, Model: {self.model}" 


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)  
        self.fuel_type = fuel_type  
        
    def get_info(self):
        return self.make + ": " + self.model + ": " + self.fuel_type 


vehicle = Vehicle("Mercedes", "G63")
print(vehicle.get_info()) 

car = Car("BMW", "M5", "Gasoline")
print(car.get_info()) 
