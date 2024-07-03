from menu import Menu

class Restaurent:
    def __init__(self,name) -> None:
        self.name=name
        self.employees=[] # eta main database
        self.menu=Menu()
        
        def add_employee(self,employee):
        # employee=Employee(name,email,phone,address,age,salary,designation)
            self.employees.append(employee)
            print(f"Employee {name} is added ! !")
            
        def view_employee(self):
            print("Employee List !!")
            for emp in self.employees:
                print(emp.name,emp.email,emp.phone,emp.address)

      
        
        
# ad = Admin('Rahim','123455','rahim@gmail,','Dhaka') 
# ad.add_employee('sagor','s@gmail.com','12344','khulna',43,23000,'Admin')     
# ad.view_employee()     
  
# res1=Restaurent('kabab house')
# bg=Menu()
# item1=Fooditems('Pizza',12,20)
# item2=Fooditems('Burgir',10,30)
# # bg.add_menu_item(item1)
# # bg.add_menu_item(item2)
# # bg.show_menu()   
# admin=Admin('admin',3434,'admin@gmail.com','DHaka')
# admin.add_menu_items(res1,item1)
# admin.add_menu_items(res1,item2)

# cus1=Customer('sakib','34567','sakib934@mail','Syllhet') 
# cus1.view_menu(res1)   

# item_name=input("Enter Item name :")
# item_quantity=int(input("Enter item quantity :"))

# cus1.add_to_cart(res1,item_name,item_quantity)
# cus1.view_cart()
    
    
                
        
                



    
        
        
