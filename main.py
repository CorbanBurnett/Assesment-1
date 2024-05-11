'''i am Creating The menu then i am adding in $8.50 pizzas then im adding in the $13.50
pizzas for the pizza resturant called "Crusty"'''
# Define a class for the pizza ordering system
class PizzaOrderingSystem:
    # Create the menu
    MENU = {
        1: ("Pepperoni", 8.50),
        2: ("Cheesy Garlic", 8.50),
        3: ("Ham and Cheese", 8.50),
        4: ("Beef and Onion", 8.50),
        5: ("Hawaiian", 8.50),
        6: ("Bacon & Aioli", 8.50),
        7: ("Classic Veggie", 8.50),
        8: ("Greasy Grove", 13.50),
        9: ("Crusty Meaty Meatlovers", 13.50),
        10: ("Crusty Sausage", 13.50),
        11: ("Crusty Veggie", 13.50),
        12: ("Pleasent Plazza", 13.50),
        13: ("3500HP GTR R35", 13.50),
        14: ("ScatPack Hellcat", 13.50),
    }

    # Start the order as an empty dictionary
    def __init__(self):
        self.order = {}
        self.customer_info = {}

    # Helper function to get the price of a pizza
    def get_pizza_price(self, pizza_name):
        for number, (pizza, price) in self.MENU.items():
            if pizza == pizza_name:
                return price
        return 0

    # Method to display Menu
    def display_menu(self):
        print("Crusty Pizza Menu:")
        # Print each pizza with its number and price
        for number, (pizza, price) in self.MENU.items():
            print(f"{number}. {pizza}: ${price:.2f}")

    # Method to take an order
    def take_order(self):
        # Get customer name
        self.get_customer_name()

        while True:
            # Ask the user to enter the pizza number they'd like to order
            pizza_number = input("Enter the pizza number you'd like to order (or 'quit' to finish ordering): ")
            # If the user wants to quit, break the loop
            if pizza_number.lower() == 'quit':
                break
            elif pizza_number.isdigit() and int(pizza_number) in self.MENU:
                pizza = self.MENU[int(pizza_number)][0]
                # Ask the user how many they'd like to order
                quantity = int(input("How many would you like to order? "))
                # If the pizza is already in the order, add the quantity
                if pizza in [p for p, _ in self.order.values()]:
                    for key, value in self.order.items():
                        if value[0] == pizza:
                            self.order[key] = (pizza, value[1] + quantity)
                            break
                else:
                    self.order[len(self.order) + 1] = (pizza, quantity)
            else:
                print("Sorry, that's not a valid pizza number.")

        # Ask the user if they want delivery and get additional info if needed
        self.add_delivery_fee()

    # Method to get customer name
    def get_customer_name(self):
        name = input("Please enter your name: ")
        self.customer_info["Name"] = name

    # Method to add delivery fee and get additional info if needed
    def add_delivery_fee(self):
        delivery = input("Would you like delivery? (yes/no) ").lower()
        if delivery == "yes":
            self.order[len(self.order) + 1] = ("Delivery Fee", 2.50)
            print("A $2.50 delivery fee has been added to your order.")
            self.get_delivery_info()
        else:
            print("No delivery fee added.")

    # Method to get delivery information
    def get_delivery_info(self):
        phone_number = input("Please enter your phone number: ")
        address = input("Please enter your delivery address: ")
        self.customer_info["Phone Number"] = phone_number
        self.customer_info["Address"] = address

    # Calculate the total price of the order
    def calculate_total(self):
        total = 0
        for _, (pizza, quantity) in self.order.items():
            if pizza != "Delivery Fee":
                total += self.get_pizza_price(pizza) * quantity
            else:
                total += quantity
        return total

    # Print the user's order and the total price
    def display_order(self):
        print("Your Order:")
        print(f"Name: {self.customer_info['Name']}")
        if "Phone Number" in self.customer_info:
            print(f"Phone Number: {self.customer_info['Phone Number']}")
        if "Address" in self.customer_info:
            print(f"Address: {self.customer_info['Address']}")
        print()
        for number, (pizza, quantity) in self.order.items():
            if pizza != "Delivery Fee":
                pizza_price = self.get_pizza_price(pizza)
                print(f"{number}. {pizza}: {quantity} x ${pizza_price:.2f} = ${pizza_price * quantity:.2f}")
            else:
                print(f"{number}. {pizza}: ${quantity:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")

# Main function to run the program
def main():
    order = PizzaOrderingSystem()
    print("Welcome to Crusty Pizza!")
    while True:
        print("\n1. Display Menu")
        print("2. Take Order")
        print("3. Display Order")
        print("4. Quit")
        choice = input("What would you like to do? ")
        if choice == '1':
            order.display_menu()
        elif choice == '2':
            order.take_order()
        elif choice == '3':
            order.display_order()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function if the script is run directly
if __name__ == "__main__":
    main()