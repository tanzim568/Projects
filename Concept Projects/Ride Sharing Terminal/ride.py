from datetime import datetime
from vehicle import Car,Bike
from time import sleep

class RideSharing :
    def __init__(self,company_name) -> None:
        self.company_name=company_name
        self.riders=[]  #  riders er ekta database jotojon ride kortese
        self.drivers=[] #  riders er ekta database jotogulo driver available ache
        self.rides=[]  #  riders er ekta database jotogulo rides complete hoise
    
    def add_rider(self,rider):
        self.riders.append(rider)
    
    def add_driver(self,driver):
        self.drivers.append(driver)
        
    def __repr__(self) -> str:
        return f"Company name {self.company_name} with riders :{len(self.riders)} and Drivers :{len(self.drivers)}"
        
class Ride:
    def __init__(self,start_location,end_location,vehicle) -> None:
        self.start_location=start_location
        self.end_location=end_location
        self.driver=None
        self.rider=None
        self.start_time=None
        self.end_time=None
        self.vehicle=vehicle
        self.estimated_fare=self.calculate_fare(vehicle.vehicle_type)
        
    def set_driver(self,driver): #driver objecr
        self.driver=driver
     
    def start_ride(self):
        self.start_time= datetime.now()
        sleep(5)
        
    def end_ride(self):
        self.end_time=datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare
        
    #total cost / Fare :
    def calculate_fare(self,vehicle_type):
        distance =10 
        # print(vehicle_type)
        fare_per_km = {
             'car': 30,
             'bike': 20,
             'cng':25
            
        }
        # return distance*fare_per_km[vehicle_type]    #self made
        return distance * fare_per_km.get(vehicle_type)     
    def __repr__(self) -> str:
        return f"Ride details -->  Started from  {self.start_location} to {self.end_location}"    
    
class RideRequest:
    def __init__(self,rider,end_location) -> None:
        self.rider=rider #rider object
        self.end_location=end_location
        
class RideMatching:
    def __init__(self,drivers) -> None:  #driver er list achhe drivers e
        self.available_drivers=drivers
    
    def find_drivers(self,ride_request,vehicle_type): #RideRequest class er object ride_request
        # print(f"from find drivers : vehicle type {vehicle_type}")
        if len(self.available_drivers)>0:
            print("Looking for Drivers . . . . ")
            driver=self.available_drivers[0]    
            
            if vehicle_type == 'car':
                vehicle=Car('car','abc354',30)
            elif vehicle_type =='bike':
                vehicle=Bike('bike','334dd',50)
                
            
            ride=Ride(ride_request.rider.cur_location,ride_request.end_location,vehicle) #ride class er object
            driver.accept_ride(ride)
            return ride
        
