MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

total_money_report = 0

def deposited_money(coffee_type): # trying to use this to update the money value in the
    # resource_report depending on what the user orders
    global total_money_report
    if coffee_type == 'espresso':
        total_money_report += MENU['espresso']['cost']
    elif coffee_type == 'latte':
        total_money_report += MENU['latte']['cost']
    elif coffee_type == 'cappuccino':
        total_money_report += MENU['cappuccino']['cost']

    return total_money_report


def quarters():
    return 0.25*int(input("How many quarters?: "))

def nickels():
    return 0.05*int(input("How many nickels?: "))

def dimes():
    return 0.10*int(input("How many dimes?: "))

def pennies():
    return 0.01*int(input("How many pennies?: "))

def money_taker():
    print("Please insert coins.")
    return quarters() + nickels() + dimes() + pennies()

def check_resources(coffee_type):
    """Check if there are enough resources to make the selected coffee."""
    for ingredient, amount in MENU[coffee_type]['ingredients'].items():
        if resources[ingredient] < amount:
            return f"Sorry, there is not enough {ingredient}"
        return True

def process_transaction(coffee_type, inserted_money):
    """Handles payment and resource deduction for a coffee order."""
    global total_money_report

    cost = MENU[coffee_type]['cost']
    if inserted_money < cost:
        return "Sorry, that's not enough money. Money refunded."
    else:
        change = round(inserted_money - cost, 2)
        total_money_report += cost
        for ingredient, amount in MENU[coffee_type]['ingredients'].items():
            resources[ingredient] -= amount
        return f"Here is ${change} in change.\nHere is your {coffee_type}. Enjoy!"

def report():
    """ Generates a report of the current resources and money."""
    resource_report = (
        f"Water: {resources['water']}ml\n"
        f"Milk: {resources['milk']}ml\n"
        f"Coffee: {resources['coffee']}g\n"
        f"Money: ${total_money_report:.2f}" # tells you how much money the machine has taken
        # (basically the sum of the costs of all the coffees ordered)
    )
    return resource_report

def user_input(user_command):
    if user_command == 'off':
        print("Shutting off. Goodbye!")
        exit()
        # end execution
    elif user_command == 'report':
        return report()
        # print resources
    elif user_command in MENU:
        resource_check = check_resources(user_coffee)
        if resource_check is not True:
            return resource_check
        total_money = money_taker()
        return process_transaction(user_coffee,total_money)
    else:
        return "Invalid input. Please try again."

while True:
    user_coffee = input("What would you like? (Espresso/Latte/Cappuccino): ").strip().lower()
    result = user_input(user_coffee)
    print(result)


