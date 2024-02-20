
class ShoeController:
    def __init__(self, shoe_model):
        self.shoe_model = shoe_model

    def add_shoe(self, shoe_id, name, size, price):
        shoe = Shoe(shoe_id, name, size, price)
        if self.shoe_model.add_shoe(shoe):
            print("Shoe added successfully!")
        else:
            print("Failed to add shoe.")

    def remove_shoe(self, shoe_id):
        self.shoe_model.remove_shoe(shoe_id)
        print("Shoe removed successfully!")

    def show_all_shoes(self):
        shoes = self.shoe_model.get_all_shoes()
        ShoeView.display_shoes(shoes)

    def show_shoes_by_size(self, size):
        shoes = self.shoe_model.get_shoes_by_size(size)
        ShoeView.display_shoes(shoes)

    def show_total_price(self):
        total_price = self.shoe_model.get_total_price()
        print("Total price of all shoes:", total_price)