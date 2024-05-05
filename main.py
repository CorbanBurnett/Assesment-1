'''i am Creating The menu then i am adding in $8.50 pizzas then im adding in the $13.50
pizzas for the pizza resturant called "Burnt"'''
class PizzaOrderingSystem:
  MENU = {
      "Peperoni": 8.50,
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
  def __init__(self):
      self.order = {}
  def display_menu(self):
      print("Burnt Pizza Menu:")
      for pizza, price in self.MENU.items():
          print(f"{pizza}: ${price:.2f}")
  def take_order(self):
      while True:
          pizza = input("Enter the pizza you'd like to order (or 'quit' to finish ordering): ")
          if pizza.lower() == 'quit': 
              break
          elif pizza in self.MENU:
              quantity = int(input("How many would you like to order? "))
              if pizza in self.order:
                  self.order[pizza] += quantity
              else:
                  self.order[pizza] = quantity
          else:
              print("Sorry, we don't have that pizza on the menu.")

      def calculate_total(self):
        total = 0
        for pizza, quantity in self.order.items():
            total += self.MENU[pizza] * quantity
        return total

      def display_order(self):
          print("Your Order:")
          for pizza, quantity in self.order.items():
              print(f"{pizza}: {quantity} x ${self.MENU[pizza]:.2f} = ${self.MENU[pizza]*quantity:.2f}")
          print(f"Total: ${self.calculate_total():.2f}")
        def main():
            order = PizzaOrder()
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

        if __name__ == "__main__":
            main()
