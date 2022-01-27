
# Menu with the resources and cost needed
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

# Resources Dict to keep track of
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# coins and their associated value
coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

customer_coins = {
    "quarters_inserted": 0,
    "dimes_inserted": 0,
    "nickles_inserted": 0,
    "pennies_inserted": 0
}

# functions ========================================================
# makes sure you have the necessary ingredients amount
def verify_enough_resources(drink):

    drink_ingredients = MENU[drink]

    for key, values in drink_ingredients["ingredients"].items():

        if values > resources[key]:
            print(f"Sorry there is not enough {key}.")
            return False

    return True

# verify if customer inserted right amount of coins, refund, ask for payment
def verify_enough_coins(drink):

    drink_cost = MENU[drink]["cost"]
    total_money = 0.0

    customer_coins = {
        "quarters": 0,
        "dimes": 0,
        "nickles": 0,
        "pennies": 0
    }

    for key, values in customer_coins.items():
        customer_coins[key] = int(input(f"how many {key}?:\t "))
        total_money += (coins[key] * customer_coins[key])

    if total_money > drink_cost:
        print(f"Here's ${total_money - drink_cost:.2f} in change.")
        return True
    elif total_money < drink_cost:
        print("Sorry, that's not enough. Money refunded.")
        return False
    else:
        return True


# functions for menu items, using resources and measuring costs
def make_choice_drink(drink):

    if verify_enough_resources(drink) and verify_enough_coins(drink):

        chosen_drink = MENU[drink]

        for key, values in chosen_drink["ingredients"].items():
            
            if key in ["water", "milk"]:
                print(key, "\t : ", values, "ml")
            elif key in ["coffee"]:
                print(key, "\t : ", values, "g")

            resources[key] -= chosen_drink["ingredients"][key]

        print(f"Here is your {drink}. Enjoy!")

# ==================================================================


machine_on = True


while machine_on:

    # gives user response to their command
    command_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if command_choice in MENU:
        make_choice_drink(command_choice)
    elif command_choice == "report":
        for key, values in resources.items():
            print(key, "\t : ", values)
    elif command_choice == "off":
        machine_on = False
    else:
        print("Invalid Command\n Please use espresso, latte, cappuccino, off or report")

