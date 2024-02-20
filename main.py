#
def main():
    shoe_model = ShoeModel()
    shoe_controller = ShoeController(shoe_model)

    # Add at least 10 shoes
    shoe_controller.add_shoe(1, "Nike Air Max", 42, 150)
    shoe_controller.add_shoe(2, "Adidas Superstar", 41, 120)
    shoe_controller.add_shoe(3, "Puma Suede", 43, 100)
    shoe_controller.add_shoe(4, "Converse Chuck Taylor", 40, 80)
    shoe_controller.add_shoe(5, "Vans Old Skool", 42, 90)
    shoe_controller.add_shoe(6, "Reebok Classic", 41, 110)
    shoe_controller.add_shoe(7, "New Balance 574", 43, 130)
    shoe_controller.add_shoe(8, "Asics Gel-Lyte", 42, 140)
    shoe_controller.add_shoe(9, "Fila Disruptor", 40, 95)
    shoe_controller.add_shoe(10, "Skechers D'Lites", 41, 75)

    # Show all shoes
    shoe_controller.show_all_shoes()

    # Show shoes by size
    shoe_controller.show_shoes_by_size(42)

    # Show total price
    shoe_controller.show_total_price()

if __name__ == "__main__":
    main()
