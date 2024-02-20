
class ShoeView:
    @staticmethod
    def display_shoes(shoes):
        if not shoes:
            print("No shoes to display.")
            return
        print("ID\tName\tSize\tPrice")
        for shoe in shoes:
            print(f"{shoe.shoe_id}\t{shoe.name}\t{shoe.size}\t{shoe.price}")