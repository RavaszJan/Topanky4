
class Shoe:
    def __init__(self, shoe_id, name, size, price):
        self.shoe_id = shoe_id
        self.name = name
        self.size = size
        self.price = price

# ShoeModel manages the data (list of shoes)
class ShoeModel:
    def __init__(self):
        self.shoes = []

    def add_shoe(self, shoe):
        # Check if shoe with same ID already exists
        if any(s.shoe_id == shoe.shoe_id for s in self.shoes):
            print("Shoe with the same ID already exists!")
            return False
        # Check if price is not negative
        if shoe.price < 0:
            print("Price cannot be negative!")
            return False
        self.shoes.append(shoe)
        return True

    def remove_shoe(self, shoe_id):
        self.shoes = [s for s in self.shoes if s.shoe_id != shoe_id]

    def get_all_shoes(self):
        return self.shoes

    def get_shoes_by_size(self, size):
        return [s for s in self.shoes if s.size == size]

    def get_total_price(self):
        return sum(s.price for s in self.shoes)