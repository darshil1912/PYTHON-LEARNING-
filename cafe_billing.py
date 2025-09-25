def demo():
    menu = {
        "Cheesy Pizza": 150,
        "Aloo Tikki Burger": 50,
        "Coke": 20,
        "White Sauce Pasta": 250,
        "Veg Sandwich": 60,
        "French Fries": 80,
        "Cold Coffee": 70,
        "Chocolate Cake": 120,
        "Spring Rolls": 90,
        "Pasta Arabia": 200
    }
    print("Welcome to the cafe !!!\n")
    for item,price in menu.items():
         print(item,":₹",price)
    
    order = "yes"
    total = 0
    while order == "yes":
        cust_choice = input("Enter your order :").title().strip()
        if cust_choice in menu:
              print(f"{cust_choice} is now ordered . Price : {menu[cust_choice]}")
              total = total + menu[cust_choice]
        else:
              print(f"Sorry Item you enter is not available")
        order = input("Do you want to order other item?").lower().strip()
        if order == "no":
             break

    print(f"Your total bill is {total}")
    print(f"THANK YOU 😃")
    
demo()