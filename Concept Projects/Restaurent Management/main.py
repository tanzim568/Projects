from fooditem import Fooditems
from menu import Menu
from user import Customer,Admin,Employee
from restaurent import Restaurent
from orders import Order

res1=Restaurent('mamar restaurent')
def customer_menu():
    name=input("\tEnter your name :")
    phone=input("\tEnter phone number :")
    email=input("\tEnter your email :")
    address=input("\tEnter address :")
    customer = Customer(name=name,phone=phone,email=email,address=address)
    
    while True:
        print()
        print(f'\n\tWelcome {customer.name}')
        print('\t1. View Menu')
        print("\t2. Add Item to cart")
        print("\t3. View cart")
        print('\t4. Paybill ')
        print("\t5. Exit\n")
        choice =int(input("\tEnter your choice :"))
        if choice ==1 :
            customer.view_menu(res1)
        elif choice ==2:
            item_name=input("\tEnter your item_name= :")
            quantity=int(input('\tEnter quantity :'))
            customer.add_to_cart(res1,item_name,quantity)
        elif choice == 3:
            customer.view_cart()   
        
        elif choice == 4:
            customer.paybill()
        elif choice == 5:
            break 
        else :
            print("Invalid Input")
            
            
            
def admin_menu():
    name=input("\tEnter your name :")
    phone=input("\tEnter phone number :")
    email=input("\tEnter your email :")
    address=input("\tEnter address :")
    admin = Admin(name=name,phone=phone,email=email,address=address)
    
    while True:
        print()
        print(f'\tWelcome to Admin Panel {admin.name}')
        print('\t1. Add New item')
        print("\t2. Add New Employee")
        print("\t3. View Employee")
        print('\t4. View Items ')
        print("\t5. Delete Items")
        print("\t6. Exit")
        choice =int(input("\n\tEnter your choice :"))
        if choice ==1 :
            name=input("\tEnter item name :")
            price=int(input('\tEnter item price :'))
            quantity=int(input('\tEnter item quantity :'))    
            item=Fooditems(name,price,quantity)
            admin.add_menu_items(res1,item)
            
        elif choice ==2:
            name=input("\tEnter name :")
            phone=input("\tEnter phone :")
            email=input("\tEnter email :")
            address=input("\tEnter address :")
            designation=input("\tEnter designation :")
            salary=input("\tEnter salary :")
            employee=Employee(name,phone,email,address,designation,salary)
            admin.add_employee(res1,employee)
          
        elif choice == 3:
            admin.view_employee(res1)  
        
        elif choice == 4:
            admin.view_items(res1)
        elif choice == 5:
            item_name=input("\tEnter item_name :")
            admin.remove_items(res1,item_name)
        elif choice == 6 :
            
            break
        else:
            print("Invalid Input")
            
while True:
    print("\t---------------------------------")
    print("\tWelcome to Mamar Restaurent ! !")
    print()
    print("\t1. Customer")
    print("\t2. Admin ")
    print("\t3. Exit\n")
    choice= int(input("\tEnter your choice :"))
    
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
   
    elif choice == 3:
        print(f'===================================')
        print(f'Thanx for visiting our restaurent !')
        print(f'===================================')
        break
    else:
        print("Invalid Inpuut")
        
        




