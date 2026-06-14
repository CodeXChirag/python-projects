
from Coffeee import MENU, resources

coffe_profit = 0
resources["profit"] = coffe_profit
coins = ["quarters", "dimes", "nickles", "pennies"]
Total=0
while True:
    coffee_type = input("What would you like? (espresso/latte/cappuccino):  ")
    if coffee_type == "off":
        print("Thank You")
        break

    flavour = ["espresso", "latte", "cappuccino"]

    def order():
        global coffe_profit
        change = Total - MENU[coffee_type]["cost"]
        coffe_profit += MENU[coffee_type]["cost"]
        resources["profit"] = coffe_profit
        print(f"Here is your ${round(change, 2)} in change.")
        print("Here is your latte ☕️. Enjoy!")


    def ingredient():
     global Total

     if coffee_type not in flavour and coffee_type != "report":
      print("Not a flavour")
      return
     elif coffee_type == "report":
      print(f"Water: {resources['water']}ml")
      print(f"Milk: {resources['milk']}ml")
      print(f"Coffee: {resources['coffee']}g")
      print(f"Money: ${resources['profit']}")
      return

     ingredients = MENU[coffee_type]["ingredients"]
     if (resources["water"] < ingredients.get("water", 0) or
             resources["milk"] < ingredients.get("milk", 0) or
             resources["coffee"] < ingredients.get("coffee", 0)):
      print("Sorry insufficient resources")
      return  # Stop here if not enough resources

     # Now ask for coins only if resources are sufficient
     print("Please insert coin")
     for i in coins:
      Money = float(input(f"How many {i}: "))
      if i == "quarters":
       Total += Money * 0.25
      elif i == "dimes":
       Total += Money * 0.10
      elif i == "nickles":
       Total += Money * 0.05
      elif i == "pennies":
       Total += Money * 0.01

     if MENU[coffee_type]["cost"] > Total:
      print("Sorry you don't have sufficient balance")
     else:
      resources["water"] -= ingredients.get("water", 0)
      resources["milk"] -= ingredients.get("milk", 0)
      resources["coffee"] -= ingredients.get("coffee", 0)
      order()


    ingredient()

