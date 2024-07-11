from ride import Ride, RideMatching, RideRequest, RideSharing
from user import Rider, Driver
from vehicle import Car,Bike
rider_zone= RideSharing('rider_zone')
rahim=Rider('Rahim Uddin','rahim@gamil.com','234566','Uttara',1200) # jatri
rider_zone.add_rider(rahim)
karim=Driver('karim uddin','karim@gamil.com','34343','Motizil')
rider_zone.add_driver(karim)
rahim.request_ride(rider_zone,'Motizil',"bike")
# rahim.show_current_ride()
karim.reach_destination(rahim.cur_ride)
rahim.show_current_ride()
print("\n",rider_zone)
