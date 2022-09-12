logo="""   
 _____          __   __             ___  ___              _      _               
/  __ \        / _| / _|            |  \/  |             | |    (_)              
| /  \/  ___  | |_ | |_  ___   ___  | .  . |  __ _   ___ | |__   _  _ __    ___  
| |     / _ \ |  _||  _|/ _ \ / _ \ | |\/| | / _` | / __|| '_ \ | || '_ \  / _ \ 
| \__/\| (_) || |  | | |  __/|  __/ | |  | || (_| || (__ | | | || || | | ||  __/ 
 \____/ \___/ |_|  |_|  \___| \___| \_|  |_/ \__,_| \___||_| |_||_||_| |_| \___|                                                                                                                                                                                                               
"""
print(logo)



menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


# prompt function
def prompt():
    action = input("What would you like? (espresso/latte/cappuccino): ")
    match action:
        case 'espresso':
            return menu['espresso']
        case 'latte':
            return menu['latte']
        case 'cappuccino':
            return menu['cappuccino']
        case 'off':
            return 'off'
        case 'report':
            return resources


def check_avail(choice):
    if choice == 'off':
        return 'off'
    elif choice == resources:
        return resources
    elif choice['ingredients']['water'] <= resources['water'] and choice['ingredients']['milk'] <= resources['milk'] \
            and choice['ingredients']['coffee'] <= resources['coffee']:
        return True
    else:
        if choice['ingredients']['water'] > resources['water']:
            print(" “Sorry there is not enough water.”")
        elif choice['ingredients']['milk'] > resources['milk']:
            print(" “Sorry there is not enough milk.”")
        elif choice['ingredients']['coffee'] > resources['coffee']:
            print("“Sorry there is not enough coffee.”")
        return False


# coin enter
def enter_coin():
    total = 0
    total += int(input("How many quarters do you want to enter:")) * 0.25
    total += int(input("How many dimes do you want to enter:")) * 0.10
    total += int(input("How many nickles do you want to enter:")) * 0.05
    total += int(input("How many pennies do you want to enter:")) * 0.01
    return total


def check_trans(amount, choices):
    if amount >= choices['cost']:
        return True
    else:
        return False


def service(menus):
    if menus == menu['espresso']:
        return 'espresso'
    elif menus == menu['latte']:
        return 'latte'
    else:
        return 'cappuccino'


# main source code

end = False  # to iterate the coffee machine operation

while not end:
    act = prompt()
    if act == menu['espresso'] or act == menu['latte'] or act == menu['cappuccino']:
        if check_avail(act):
            print("Please enter coins")
            coin = enter_coin()
            if check_trans(coin, act):
                print(f"Here is ${round(coin, 2)} in change.")
                print(f"Here is your {service(act)} ☕️. Enjoy!")
                resources['water'] = resources['water'] - act['ingredients']['water']
                resources['coffee'] = resources['coffee'] - act['ingredients']['coffee']
                resources['milk'] = resources['milk'] - act['ingredients']['milk']
            else:
                print("Sorry that's not enough money. Money refunded.")

    elif act == resources:
        for item in resources:
            print("{} : {}".format(item, resources[item]))
    else:
        print("The coffee machine is {}".format(act))
        end = True
