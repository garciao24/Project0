from rich.console import Console
from rich.table import Table
    
    
c = Console()

    
class menu():
    
    def menu(self):
        c.print("--------Pizzeria Main Menu-----------",style='light_sea_green')
        c.print("Select an option")
        c.print("Customer Menu 1")
        c.print("Items Menu 2")
        c.print("Orders Menu 3")
        c.print("Take New Order 4")
        c.print("EXIT 5")
        c.print("-------------------")

    def customer_menu(self):
        c.print("-------Customer menu---------",style='light_sea_green')
        c.print("Select an option")
        c.print("Show Customers 1")
        c.print("Add Customer 2")
        c.print("Delete Customer 3")
        c.print("Modify Customer 4")
        c.print("Back to main menu 5")
        c.print("-------------------")

    def items_menu(self):
        c.print("-----Items menu--------------",style='light_sea_green')
        c.print("Select an option")
        c.print("Show Items 1")
        c.print("Add Items 2")
        c.print("Delete Item 3")
        c.print("Modify Item 4")
        c.print("Back to main menu 5")
        c.print("-------------------")

    def orders_menu(self):
        c.print("-----Orders menu--------------",style='light_sea_green')
        c.print("Select an option")
        c.print("Show Orders 1")
        c.print("Take New Order 2")
        c.print("Delete Orders 3")
        c.print("modify Orders 4")
        c.print("Back to main menu 5")
        c.print("-------------------")

