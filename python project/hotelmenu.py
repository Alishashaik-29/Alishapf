# define the menu of restaurent
menu ={
    'Pizza': 50,
    'pasta': 60,
    'Burger':60,
    'Noodles':90,
    'Coffee':60,
    'Soft drinks':45,
    'lemon soda':40,
    

}

#Greet
print("Welcome to CHAI CUPS")
print("pizza: Rs50\npasta: Rs60\nBurger: Rs60\nNoodles: Rs90\nCoffee: Rs60\nSoft drinks: Rs45\nlemon soda: Rs40")

order_total = 0


item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not avaliable yet!")

another_order = input("Do you want to add another item? (Yes/No) ")

if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount of items to pay is {order_total}")






