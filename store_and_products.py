# Create Store Class

class Store:
    def __init__(self, name):
        self.name = name
        self.list = []

    def add_product(self, new_product):
        self.list.append(new_product)
        return self
    
    def sell_product(self, id):
        self.list.pop(id)
        return self
    
    def print_products(self):
        for i in store.list:
            i.print_info()
        
    def inflation(self, percent_increase):
        for i in store.list:
            i.update_price(percent_increase, True)
    
    def set_clearance(self, category, percent_discount):
        for i in store.list:
            if category == category:
                i.update_price(percent_discount, False)
    
# Create Product Class

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price = self.price + (self.price * percent_change)
        if is_increased == False:
            self.price = self.price - (self.price * percent_change)
        return self
    
    def print_info(self):
        print("Product Name: " + self.name)
        print("Category: " + self.category)
        print("Price: $" + str(self.price))
        return self

# Create 1 instance of Store and 3 of Product

store = Store("Julia's Store")

product1 = Product("Cheerios", 5, "Cereal")
product2 = Product("Rice Krispies", 4, "Cereal")
product3 = Product("Chex", 6, "Cereal")

# Test Product Methods

product1.print_info()
product2.update_price(.05, True).print_info()
product3.update_price(.05, False).print_info()

# Test Store Methods

store.add_product(product1)
store.add_product(product2)
store.add_product(product3)
store.print_products()

store.sell_product(0)
store.print_products()

store.inflation(.05)
store.print_products()

store.set_clearance("Cereal", .5)
store.print_products()

