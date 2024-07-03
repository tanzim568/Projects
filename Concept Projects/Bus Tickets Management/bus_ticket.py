from abc import ABC,abstractmethod

class AbstractBus(ABC):
    def __init__(self,coach,driver,arrival,from_des,to) -> None: #here none means je constructor kono kisu return kore na
        self.coach=coach
        self.driver=driver
        self.arrival=arrival
        self.from_des=from_des
        self.to=to
        self.seats=["empty" for _ in range(20)]
   
class Bus(AbstractBus):
    pass  # bus initialize na korle def __init__ constractor declare korle super keyword diye parameter base class e par kora kora lage pass dile oi full class tai derived class ba bus class inherit korbe.. ekhne full abstractbus class ta bus class inherit kortese


class BusCompany:
    def __init__(self) -> None:
        self.buses={} # sokol bus details thakbe & as a database kaj korbe
    
    
    def install_bus(self,bus): #ekhan amra mainly bus class er object pathabo ar sei object er key hisebe dictionary te self.coach er value ba coach rakhbo
        self.buses[bus.coach]=bus  #dictionary er ekpashe thkbe coach no other side e thakbe bus(object of bus class) object.coach=(jei value setai dictionry key hisebe initiallize hobe)
             
         
    def display_available_buses(self):     
             
        if not self.buses:     
            print("No buses available! !")
            
        else:
            print(f"Coach\tDriver\tArrival\tFrom\tTo")
            for coach,bus in self.buses.items():
                print(f"{coach}\t{bus.driver}\t{bus.arrival}\t{bus.from_des}\t{bus.to}")
    
    def book_ticket(self,coach,seat):
        if coach in self.buses:
            if 1<=seat<=20:
                if self.buses[coach].seats[seat-1] =="empty":   #   if (self.buses[coach]).seats[seat-1] =="empty": 
                    self.buses[coach].seats[seat-1]="booked"    #          uporer eituk self.buses[coach] ei part ti mainly self.buses name je dictionary niechi amra sei dictinary r value ke present korbe then value.seats[seats-1] ja mainy Bus class er object (ja dictionary value part e chilo) then oi object diye bus class dukbe then inheritance e abstractbus class e giye seats ke dhorbe
                    
                else:
                    print("Seat already Booked !")
            else:
                print("Invalid seat number !")
        else:
            print("Invalid bus coach number")
            
    def display_seat_status(self,coach):
        if coach in self.buses:
            print(self.buses[coach].seats)
            
            
bus1=Bus(2,"rahim","9pm","9.30pm","Dhaka")
company=BusCompany()
company.install_bus(bus1)

print(company.display_available_buses())
print(company.display_seat_status(2))
            
            
while True:
    print("Welcome to Bus Ticket Booking system! !")
    print("1. Install Bus")
    print("2. View Available Bus")
    print("3. Book Ticket")
    print("4. Check Seat Status")
    print("5. Exit")
    
    op=int(input("Enter choice :"))
  
        
        
                    
                
            
                
        
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
     
    # @abstractmethod
    # def install_bus(self,coach,driver,arrival,from_des,to): 
    #     pass
    
    # @abstractmethod
    # def display_available_buses(self):
    #     pass
    
    # @abstractmethod
    # def display_seat_status(self):
    #     pass             
    
    
    
        # def install_bus(self, coach, driver, arrival, from_des, to):
    #     print(f"Bus {coach} installed successfully ! ")
