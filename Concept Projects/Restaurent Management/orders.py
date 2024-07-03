class Order:
    def __init__(self) -> None:
        self.item={}
    
    def add_item(self,item):
        if item in self.item:
            self.item[item] += item.quantity  # jdi item cart e already thake then quantity 1 kore barbe
        else:
            self.item[item] = item.quantity # jdi item cart e na thake  
    
    def remove(self,item):
        if item in self.item:
            del self.item[item]
    
    def total_price(self):
        return sum(item.price * quantity for item,quantity in self.item.items()) 
    
    def clear(self):
        self.item={}
