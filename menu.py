from rich.console import Console
from os import system
from delete import delete
from input import insert
from show import show

c = Console()

class menu():

    def menu(self):
        c.print("--------Main Menu-----------",style='light_sea_green')
        c.print("Select an option")
        c.print("Customer Menu 1")
        c.print("Items Menu 2")
        c.print("Orders Menu 3")
        c.print("Take New Order 4")
        c.print("EXIT 5")
        c.print("-------------------")

    def customer_menu(self):
        c.print("-----Customer menu--------------",style='light_sea_green')
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
        c.print("Modify Orders 4")
        c.print("Back to main menu 5")
        c.print("-------------------")


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
                system('cls')
                
                show().showCustomer()

            elif option == 3:
                system('cls')
                delete().delCustomer()

            elif option == 4:
                system('cls')


            elif option == 5:
                system('cls')
                break
            else:
                print('Invalid option. Please enter a number between 1 and 5.')    


    def itemOption(self):
        while(True):
            #print('Handle option \'Option 1\'')
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
                system('cls')
                show().showItems()

            elif option == 3:
                system('cls')
                delete().delItems()

            elif option == 4:
                system('cls')

            elif option == 5:
                system('cls')
                break
            else:
                print('Invalid option. Please enter a number between 1 and 5.')    

    def orderOption(self):
        while(True):
            #print('Handle option \'Option 1\'')
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

            elif option == 5:
                system('cls')
                break
            else:
                print('Invalid option. Please enter a number between 1 and 5.')   






















