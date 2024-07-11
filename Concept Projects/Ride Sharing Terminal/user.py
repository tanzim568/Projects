from abc import ABC,abstractmethod
from ride import RideRequest,RideMatching

class User(ABC): # ABSTRACT BASE CLASS JAR KONO OBJECT DECLARE KORA JBE NA
    def __init__(self,name,email,nid) -> None:
        self.name=name
        self.email=email
        self.nid=nid
        self.wallet=0
        
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
class Rider(User): 
    def __init__(self, name, email, nid,cur_location,initial_amount) -> None:
        super().__init__(name, email, nid)  
        self.cur_ride=None
        self.cur_location=cur_location
        self.wallet=initial_amount
        
    def display_profile(self):
        # return super().display_profile()
        print(f"Rider : {self.name} and email : {self.name}")
        
    def load_cash(self,amount):
        if amount > 0:
            self.wallet += amount
        else:
            print("balance is less than 0")
    def update_location(self,current_location):
        self.cur_location=current_location

    def request_ride(self,ride_sharing,destination,vehicle_type):
        # print(f"{vehicle_type}") vehicle peyeche
        ride_request=RideRequest(self,destination)
        ride_matching=RideMatching(ride_sharing.drivers)
        ride=ride_matching.find_drivers(ride_request,vehicle_type)
        self.cur_ride=ride
        ride.rider=self
        print("Yay ! We got a RIDE ! ! !")
    
    def show_current_ride(self):
        print(self.cur_ride)
        print(f"Passenger : {self.name}")
        print(f"Driver : {self.cur_ride.driver.name}")
        print(f"Selected Car : {self.cur_ride.vehicle.vehicle_type} \tLicense :{self.cur_ride.vehicle.license_plate}")
        print(f"Start Location : {self.cur_ride.start_location} \t Destination {self.cur_ride.end_location}")
        print(f"Starting time {self.cur_ride.start_time} Reached at {self.cur_ride.end_time}")
        print(f"Total Fare tk\= {self.cur_ride.estimated_fare}")
        
        
class Driver(User):
    def __init__(self, name, email, nid,cur_location,) -> None:
        super().__init__(name, email, nid)
        self.cur_location=cur_location
        self.wallet=0
        
    def display_profile(self):
        # return super().display_profile()
        print(f"Dirver Name :{self.name} ")
        
    def accept_ride(self,ride):
        #need to accept rides from user
        # pass
        ride.start_ride()
        ride.set_driver(self)   #ei driver er object ke pathachii mane ei driver request accept koreche tai oi ride e ei driver set kora hoyechge
    
    
    def reach_destination(self,ride):
        ride.end_ride()