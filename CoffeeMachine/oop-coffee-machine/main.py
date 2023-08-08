from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
my_menu = Menu()


# Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
is_on = True
while is_on:
    menu_items = my_menu.get_items()
    choice = input(f"What would you like? ({menu_items}): ")
    # Turn off the Coffee Machine by entering “ off ” to the prompt.
    if choice == "off":
        is_on = False
    # Print report.
    elif choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(choice)
        if my_coffee_maker.is_resource_sufficient(drink):
            payment = my_money_machine.make_payment(drink.cost)
            if payment:
                my_coffee_maker.make_coffee(drink)