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
          for pizza, price in self.menu.items():
              print(f"{pizza}: ${price:.2f}")

      def take_order(self):
          while True:
            pizza = input("Enter the pizza you'd like to order (or 'quit' to finish ordering): 
            ")
              if pizza.lower() == 'quit':
