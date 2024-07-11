from abc import ABC,abstractmethod

class Vehicle(ABC):
    speed = {  #speed ekti class variable jeta vehicle ke inherit kora sob class use krte par   
        'car':50,
        'bike':60,
        'cng':15
    }
    def __init__(self,vehicle_type, license_plate, rate ) -> None:  
        self.vehicle_type=vehicle_type
        self.license_plate=license_plate
        self.rate=rate
        

class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
        
class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
        
    