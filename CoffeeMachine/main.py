from menu_data import MENU
profit = 0
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
def report():
    return f"Water: {resources['water']} \nMilk: {resources['milk']} \nCoffee: {resources['coffee']} \nProfit: {profit}"


def resource_check(ingredient_list):
    for item in ingredient_list:
        if ingredient_list[item] > resources[item]:
            return False
        else:
            return True
    
def money_check():
    total = 0
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def transaction(drink_cost, money_received):
    if money_received >= drink_cost:
        change = round((money_received - MENU['latte']['cost']), 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

         
def resource_manage(ingridient_list):
    for item in ingridient_list:
        resources[item] -= ingridient_list[item]



def cust_choice():
    should_continue = True
    while should_continue:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

        if choice == 'report':
            print(report())
        elif choice == 'off':
            should_continue = False
        else:
            drink = MENU[choice]
            if resource_check(drink['ingredients']):
                money_given = money_check()
                if transaction(drink['cost'], money_given):
                    resource_manage(drink['ingredients'])
                    print(f"Here is your {choice} ☕️. Enjoy!")
            else:
                should_continue = False
                print("Sorry, I do not have enough resources for recipe")
            
cust_choice()