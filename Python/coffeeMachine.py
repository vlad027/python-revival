import sys

QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit": 0
}

def report():
    for key in resources:
        if key == "water" or key == "milk":
            print(f"{key.capitalize()}: {resources[key]}ml")
        elif key == "coffee":
            print(f"{key.capitalize()}: {resources[key]}g")
        elif key == "profit":
            print(f"{key.capitalize()}: ${resources[key]:.2f}")

def turn_off():
    sys.exit("The machine is now off")

def check_resources(user_choice):
    ingredients = MENU[user_choice]["ingredients"]
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?  "))
    dimes = int(input("How many dimes?  "))
    nickels = int(input("How many nickels?  "))
    pennies = int(input("How many pennies?  "))
    
    total = (QUARTER * quarters) + (DIME * dimes) + (NICKEL * nickels) + (PENNY * pennies)
    return total

def process_transaction(user_choice):
    total_inserted = process_coins()
    drink_price = MENU[user_choice]["cost"]

    if total_inserted >= drink_price:
        refund = round(total_inserted - drink_price, 2)
        resources["profit"] += drink_price
        if refund > 0:
            print(f"Here is ${refund:.2f} in change.")
        return True
    else:
        print(f"Insufficient funds. Refunding ${total_inserted:.2f}")
        return False

def update_resources(user_choice):
    ingredients = MENU[user_choice]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]

def get_user_choice():
    return input("What would you like? (espresso/latte/cappuccino/report/off): ").lower()

def coffee_machine():
    while True:
        user = get_user_choice()

        if user == "off":
            turn_off()
        elif user == "report":
            report()
        elif user in MENU:
            if check_resources(user):
                if process_transaction(user):
                    update_resources(user)
                    print(f"Here is your {user.capitalize()}. Enjoy!")
        else:
            print("Invalid selection. Please choose espresso, latte, cappuccino, report, or off.")

coffee_machine()
