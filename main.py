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
resources.update({"money": 0})
MENU['espresso']['ingredients']['milk'] = 0

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01


def report(dictionary):
    key_list = []
    for item in dictionary:
        key = str(item)
        key = key.capitalize()
        key_list.append(key)
    print(f"{key_list[0]}: {dictionary['water']}ml")
    print(f"{key_list[1]}: {dictionary['milk']}ml")
    print(f"{key_list[2]}: {dictionary['coffee']}g")
    print(f"{key_list[3]}: ${dictionary['money']}")


def ingredient_check(drink):
    water_wanted = MENU[drink]['ingredients']['water']
    milk_wanted = MENU[drink]['ingredients']['milk']
    coffee_wanted = MENU[drink]['ingredients']['coffee']
    if resources['water'] < water_wanted:
        print(f"Sorry there is not enough water.")
        return False
    if resources['milk'] < milk_wanted:
        print(f"Sorry there is not enough milk.")
        return False
    if resources['coffee'] < coffee_wanted:
        print(f"Sorry there is not enough coffee.")
        return False
    return True


def coin_exchange(cents25, cents10, cents05, cents01, drink, materials):
    total_quarters = cents25*quarters
    total_dimes = cents10*dimes
    total_nickles = cents05*nickles
    total_pennies = cents01*pennies
    total_money = total_quarters + total_dimes + total_nickles + total_pennies
    purchase_change = round(total_money - MENU[drink]['cost'], 2)
    if purchase_change >= 0:
        print(f"Here is ${purchase_change} in change.")
        print(f"Here is your {drink} ☕. Enjoy!")
        materials['money'] += MENU[drink]['cost']
        return True
    elif purchase_change < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False


def resources_remaining(water_consumed, milk_consumed, coffee_consumed, res_dict):
    res_dict['water'] = res_dict['water'] - water_consumed
    res_dict['milk'] = res_dict['milk'] - milk_consumed
    res_dict['coffee'] = res_dict['coffee'] - coffee_consumed


def used_materials(beverage_choice, materials_dictionary):
    water_used = MENU[beverage_choice]['ingredients']['water']
    milk_used = MENU[beverage_choice]['ingredients']['milk']
    coffee_used = MENU[beverage_choice]['ingredients']['coffee']
    resources_remaining(water_used, milk_used, coffee_used, materials_dictionary)
    return materials_dictionary


using_machine = True
while using_machine:
    user_drink_choice = input("What would you like? (espresso/latte/cappuccino? ")
    if user_drink_choice == "off":
        using_machine = False
    elif user_drink_choice == "report" and using_machine is True:
        report(resources)
    elif ingredient_check(user_drink_choice):
        print("Please insert coins.")
        user_quarters = int(input("How many quarters?: "))
        user_dimes = int(input("How many dimes?: "))
        user_nickles = int(input("How many nickles?: "))
        user_pennies = int(input("How many pennies?: "))
        if coin_exchange(user_quarters, user_dimes, user_nickles, user_pennies, user_drink_choice, resources):
            used_materials(user_drink_choice, resources)
