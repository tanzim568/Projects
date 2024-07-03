#projects that can normally run on terminal based systems that is known as concept project

class User:
    def __init__(self,id,name,password) -> None:
        self.id=id
        self.name=name
        self.password=password
        
class Book:
    def __init__(self,cat,id,name) -> None:
        self.cat=cat
        self.id=id
        self.name=name

class Admin:
    def __init__(self,id,name,password) -> None:
        self.id=id
        self.name=name
        self.password=password

class Library:
    def __init__(self,owner,name) -> None:
        self.owner=owner
        self.name=name
        self.users=[]
        self.books=[]
        self.borrowedlist=[]
        self.admins=[]
    
    def auth(self,id,name,password):
        admin=Admin(id,name,password)
        self.admins.append(admin)
        return admin
        
        
        
    def addUser(self,id,name,password):
        user=User(id,name,password)
        self.users.append(user)
        return user
        
    def addBook(self,cat,id,name):
        book=Book(cat,id,name)
        self.books.append(book)

lib=Library('principal','bedar')
rahim=lib.addUser(54,'rahim',1234)
admin=lib.auth(10,'ratul',5678)
lib.addBook("Thriller",23,'Birbol')
print(admin.password)

currentUser=None
run=True


while run:
    if currentUser==None:
        
        print("\n\t----------------------")
        print("\n\t Welcome to the System\n")
        print(" \t------------------------")
        option =input("\n\tRegister ? / Log In (R/L)")
        
        if option == 'R':
            id=int(input("\tEnter an ID :"))
            name=input("\tEnter your name :")
            password=input("\tEnter password :")
            
            
            
            user=lib.addUser(id,name,password)
            currentUser=user
            print(f"\n\tAccount Creation Succesfull  ")
            print(f"\t----Welcome to the system {name} ----")
            print("\n\t1. Borrow Books")
            print("\n\t2. Return Books")
            print("\n\t3. showborrowed Books")
            print("\n\t4. Logout")
            
            op=int(input("choose :"))
            if op == 1:
                id=input("Enter book id :")
                for book in lib.books:
                    if book.id == id:
                        lib.books.remove (book)
                        lib.borrowedlist.append(book)
            if op==3:
                print(list(lib.borrowedlist))
                        
                                    
            
        elif option == 'L':
            print("\n1. Admin")
            print("\n2. User")
            op=int(input())
            if op==1:
                name=input("Admin name :")
                password=int(input("Password :"))
                for admin in lib.admins:
                    # print("for paise")
                    if admin.password==password:
                        print("Welcome Back",admin.name)
                        currentUser="admin" 
                        
                print("Admin not found !") 
                
                
            if op==2:
                name=input("\tEnter your name :")
                password=int(input("\tEnter password :"))
                match=False
                for users in lib.users:
                    if users.name==name and users.password==password:
                    
                        currentUser=users.name
                        match=True
                        print(f"\n\t----Welcome to the system {name} ----")
                        print("\n")
                        print("\t1. Borrow Books")
                        print("\t2. Return Books")
                        print("\t3. showborrowed Books")
                        print("\t4. Logout")
                if match==False:
                    print("\n\tNo user found ! try again or register")
    elif currentUser == 'admin':
        print(f"Welcome Back Admin ")
        
    else:
        print(f"\t----Welcome to the system {name} ----")
        print("\n\t1. Borrow Books")
        print("\n\t2. Return Books")
        print("\n\t3. showborrowed Books")
        print("\n\t4. Logout")
        
        op=int(input("choose -:"))
        if op == 1:
            id=int(input("Enter book id :"))
            for book in lib.books:
                print(book.id)
                if book.id == id:
                    lib.books.remove(book)
                    lib.borrowedlist.append(book)
                    print("borrowed")
        if op==3:
            for book in lib.borrowedlist:
                print(book.name)
        if op==4:
            print("Logged Out")
            currentUser=None
  
            
        
    
    
    

