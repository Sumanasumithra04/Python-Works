# Define the menu of the cafe
menu = {
    'Pizza': 90,
    'Pasta': 60,
    'Burger': 80,
    'Cold drinks': 50,
    'Coffee': 50,
    'Sandwich': 60,
    'Nuggets': 70,
    'Salad': 50
}

print("Welcome to Hub Cafe")
print("Pizza: Rs90\nPasta: Rs60\nBurger: Rs80\nCold drinks: Rs50\nCoffee: Rs50\nSandwich: Rs60\nNuggets: Rs70\nSalad: Rs50")

order_total = 0

item_1 = input("Enter the name of the item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Ordered item '{item_1}' is not available yet!")

another_order = input("Do you want to add another item? (Yes/No): ")
if another_order.lower() == "yes":
    item_2 = input("Enter the name of the second item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item '{item_2}' has been added to your order.")
    else:
        print(f"Ordered item '{item_2}' is not available.")
else:
    print("No additional items added.")

print(f"The total amount to pay is Rs{order_total}")
