from rich.console import Console
from os import system
from delete import delete
from insert import insert
from modify import modify
from show import show
from rich.table import Table

c = Console()

class menu():


    def menu(self):
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Pizzeria Main Menu", justify='center', width=18)
        table.add_row(
            " [blue]Customer Menu[/blue]  [bold green]1[/bold green]"
        )
        table.add_row(
            "    [blue]Items Menu[/blue]  [bold green]2[/bold green]"
        )
        table.add_row(
            "   [blue]Orders Menu[/blue]  [bold green]3[/bold green]"
        )
        table.add_row(
            "[blue]Take New Order[/blue]  [bold green]4[/bold green]"
        )
        table.add_row(
            "          [blue]EXIT[/blue]  [bold green]5[/bold green]"
        )
        c.print(table)


    def customer_menu(self):
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Customer menu", justify='center', width=18)
        table.add_row(
            " [blue]Show Customers[/blue] [bold green]1[/bold green]"
        )
        table.add_row(
            "   [blue]Add Customer[/blue] [bold green]2[/bold green]"
        )
        table.add_row(
            "[blue]Delete Customer[/blue] [bold green]3[/bold green]"
        )
        table.add_row(
            "[blue]Modify Customer[/blue] [bold green]4[/bold green]"
        )
        table.add_row(
            "     [blue] Main Menu[/blue] [bold green]5[/bold green]"
        )
        c.print(table)


    def items_menu(self):
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Items menu", justify='center', width=18)
        table.add_row(
            "     [blue]Show Items[/blue] [bold green]1[/bold green]"
        )
        table.add_row(
            "      [blue]Add Items[/blue] [bold green]2[/bold green]"
        )
        table.add_row(
            "    [blue]Delete Item[/blue] [bold green]3[/bold green]"
        )
        table.add_row(
            "    [blue]Modify Item[/blue] [bold green]4[/bold green]"
        )
        table.add_row(
            "     [blue] Main Menu[/blue] [bold green]5[/bold green]"
        )
        c.print(table)


    def orders_menu(self):
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Orders menu", justify='center', width=18)
        table.add_row(
            "    [blue]Show Orders[/blue] [bold green]1[/bold green]"
        )
        table.add_row(
            " [blue]Take New Order[/blue] [bold green]2[/bold green]"
        )
        table.add_row(
            "  [blue]Delete Orders[/blue] [bold green]3[/bold green]"
        )
        table.add_row(
            "     [blue] Main Menu[/blue] [bold green]4[/bold green]"
        )
        c.print(table)


    def cusOption(self):
        while(True):
            #print('Handle option \'Option 1\'')
            self.customer_menu()
            option = ''
            try:
                option = int(input("please make a choice >>"))
            except:
                print('Wrong input. Please enter a number ...')
                #Check what choice was entered and act accordingly
            if option == 1:
                system('cls')
                show().showCustomer()
            
            elif option == 2:
                system('cls')
                insert().insertCustomer()
                show().showCustomer()

            elif option == 3:
                system('cls')
                delete().delCustomer()

            elif option == 4:
                system('cls')
                modify().custUpdate()

            elif option == 5:
                system('cls')
                break
            else:
                print('Invalid option. Please enter a number between 1 and 5.')    


    def itemOption(self):
        while(True):
            self.items_menu()
            option = ''
            try:
                option = int(input("please make a choice >>"))
            except:
                print('Wrong input. Please enter a number ...')
                #Check what choice was entered and act accordingly
            if option == 1:
                system('cls')
                show().showItems()
            
            elif option == 2:
                system('cls')
                insert().insertItems()
                #system('cls')
                show().showItems()

            elif option == 3:
                system('cls')
                delete().delItems()

            elif option == 4:
                system('cls')
                modify().itemUpdate()

            elif option == 5:
                system('cls')
                break
            else:
                print('Invalid option. Please enter a number between 1 and 5.')    

    def orderOption(self):
        while(True):
            self.orders_menu()
            option = ''
            try:
                option = int(input("please make a choice >>"))
            except:
                print('Wrong input. Please enter a number ...')
                #Check what choice was entered and act accordingly
            if option == 1:
                system('cls')
                show().showOrders()
            
            elif option == 2:
                system('cls')
                insert().insertOrder()
                print("Order Added")

            elif option == 3:
                system('cls')
                delete().delOrders()

            elif option == 4:
                system('cls')
                break
            else:
                print('Invalid option. Please enter a number between 1 and 4.')   
