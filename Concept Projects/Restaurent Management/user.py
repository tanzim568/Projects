from abc import ABC
from orders import Order

class User(ABC):
    def __init__(self,name,phone,email,address) -> None:
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
        
    
class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary) -> None:
        self.age=age
        self.designation=designation
        self.salary=salary 
        super().__init__(name, phone, email, address)
    
class Admin(User):
    def __init__(self, name, phone, email, address) -> None:
        super().__init__(name, phone, email, address)
        # self.employees=[] # this will be used as database of whole system
        
    def add_employee(self,restaurent,employee):
        restaurent.add_employee(employee)
      
    
    def view_employee(self,restaurent):
        restaurent.view_employee()
         
    def add_menu_items(self,restaurent,item):
        restaurent.menu.add_menu_item(item)
      
    def remove_items(self,restaurent,item_name):
        restaurent.menu.remove_items(item_name) 
    
    def view_items(self,restaurent):
        restaurent.menu.show_menu()

# sokol jabotio function restaurent classs er modde thakbe admin just oi class er modde theke call korbe
# means je eto kichu admin er janar proyoujon nei,, oi just call krbe ar kaj hoe jabe .. details sob function abstract kre rakchi amra.. sob function ekta class e gusay raksi
 
 
class Customer(User):
    def __init__(self, name, phone, email, address) -> None:
        super().__init__(name, phone, email, address)
        self.cart=Order()  #hope a dictionary will be taken after while
        
    def view_menu(self,restaurent):
        restaurent.menu.show_menu()
        
    def add_to_cart(self,restaurent,item_name,quantity):
        item=restaurent.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Quantity exceeded !!")
            else:
                item.quantity=quantity
                self.cart.add_item(item)
                print(f"{item.name} is added")
        else:
            print("Not found !")
            
    def paybill(self):
        print (f'\n\t{self.cart.total_price()} paid successfully ! !')
        self.cart.clear()
        
    def view_cart(self):
        print("\n\t**** view cart ****")
        print("\n\tName\tPrice\tQuantity") 
        for item,quantity in self.cart.item.items():
            print(f'\t{item.name} \t{item.price} \t{quantity}')  # quantity will be taken from user 
        print(f'\n\tTotal Price :{self.cart.total_price()}')
        
  