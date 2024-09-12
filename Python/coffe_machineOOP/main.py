from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()
menu_item = MenuItem()

options = menu.get_items()

is_on = True


while is_on:
    user_choice = input(f"What would you like? ({options})")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        if user_choice in options:
            sufficient_resources = coffee_maker.is_resource_sufficient(user_choice)
            if sufficient_resources == True:
                money_received = money_machine.process_coins()
                money_machine.make_payment(menu_item.cost)
                #TODO: finish the rest
                
'''OOP version of coffee machine'''
