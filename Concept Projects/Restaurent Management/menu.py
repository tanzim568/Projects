class Menu:
    def __init__(self):
        self.items=[] #menu class er database
        
    def add_menu_item(self,item):
        self.items.append(item)
    
    def find_item(self,item_name):
        for item in self.items:
            if item_name.lower() == item.name.lower():
                return item
        return f'Item not found ! '
    
    def remove_item(self,item_name):
        item = self.find_item(item_name)
        
        if item: # jdi self.find_item theke item pawa jai then 
            self.items.remove(item)
            print(f'{item.name} deleted successfully !')
        
        else:
            print("this item is not in list !")
        
    def show_menu(self):
        print("\n\t*****  Menu *******")
        print("\tName\tPrice\tQuantity")
        for item in self.items:
            print(f'\t{item.name}\t{item.price}\t{item.quantity}')
