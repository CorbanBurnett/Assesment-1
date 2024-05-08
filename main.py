'''i am Creating The menu then i am adding in $8.50 pizzas then im adding in the $13.50
pizzas for the pizza resturant called "Burnt"'''
# Define a class for the pizza ordering system
class PizzaOrderingSystem:
  #create the menu
    MENU = {
        "Pepperoni": 8.50,
        "Cheesy Garlic": 8.50,
        "Ham and Cheese": 8.50,
        "Beef and Onion": 8.50,
        "Hawaiian": 8.50,
        "Bacon & Aioli": 8.50,
        "Classic Veggie": 8.50,
        "Greasy Grove": 13.50,
        "Burnt Meaty Meatlovers": 13.50,
        "Burnt Sausage": 13.50,
        "Burnt Veggie": 13.50,
        "Pleasent Plazza": 13.50,
        "3500HP GTR R35": 13.50,
        "ScatPack Hellcat": 13.50,
    }
#start the order as an empty dictionary
    def __init__(self):
        self.order = {}
    #method to display Menu
    def display_menu(self):
        print("Burnt Pizza Menu:")
        #print each pizza with its price
        for pizza, price in self.MENU.items():
            print(f"{pizza}: ${price:.2f}")
    # Method to take an order
    def take_order(self):
        while True:
            # Ask the user to enter the pizza they'd like to order
            pizza = input("Enter the pizza you'd like to order (or 'quit' to finish ordering): ")
             # If the user wants to quit, break the loop
            if pizza.lower() == 'quit':
                break
            elif pizza in self.MENU:
                 # Ask the user how many they'd like to order
                quantity = int(input("How many would you like to order? "))
                # If the pizza is already in the order, add the quantity
                if pizza in self.order:
                    self.order[pizza] += quantity
                else:
                    self.order[pizza] = quantity
            else:
                print("Sorry, we don't have that pizza on the menu.")
#calculate the total price of the order
    def calculate_total(self):
        total = 0
        for pizza, quantity in self.order.items():
            total += self.MENU[pizza] * quantity
        return total
#print the users order and the total price
    def display_order(self):
        print("Your Order:")
        for pizza, quantity in self.order.items():
            print(f"{pizza}: {quantity} x ${self.MENU[pizza]:.2f} = ${self.MENU[pizza]*quantity:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")
# Main function to run the program
def main():
    order = PizzaOrderingSystem()
    print("Welcome to Burnt Pizza!")
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