from rich.console import Console
from os import system
from database import sql
from collections import namedtuple
import re
import string
from misc import phone


c = Console()
dp = sql()
#dp.query("SELECT * FROM customer")

def menu():
    c.print("-------------------",style='light_sea_green')
    c.print("Select an option")
    c.print("Customer Menu 1")
    c.print("Items Menu 2")
    c.print("Take New Order 3")
    c.print("EXIT 4")
    c.print("-------------------")

def customer_menu():
    c.print("-----Customer menu--------------",style='light_sea_green')
    c.print("Select an option")
    c.print("Show Customers 1")
    c.print("Add Customer 2")
    c.print("Delete Customer 3")
    c.print("Modify Customer 4")
    c.print("Back to main menu 5")
    c.print("-------------------")
    

# option = c.input("please make a choice >>")

#customer = namedtuple('Customer',['fname', 'lname', 'phone', 'Address'])
#c = customer('Nandini', '19', '2541997')


def cusOption():
    while(True):
        #print('Handle option \'Option 1\'')
        customer_menu()
        option = ''
        try:
            option = int(input("please make a choice >>"))
        except:
            print('Wrong input. Please enter a number ...')
            #Check what choice was entered and act accordingly
        if option == 1:
            system('cls')
            dp.test("SELECT * FROM customer")

        ###
           
        elif option == 2:
            system('cls')
            option2()
            
            fname, lname = input("Enter two values: ").split()
            phon = phone().input()
            Address = input("Enter Address")
            customer= (fname, lname, phon, Address)

            #dp.test("INSERT INTO customer (fname, lname, phone, Address) VALUES "+ c._fields)
            print(c)
            print("INSERT INTO customer (fname, lname, phone, Address) VALUES "+ str(customer))
            



        elif option == 3:
            system('cls')
            option3()

        elif option == 4:
            system('cls')


        elif option == 5:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')    


def option2():
     print('Handle option \'Option 2\'')

def option3():
     print('Handle option \'Option 3\'')



system('cls')
if __name__=='__main__':
    while(True):
        
        menu()
        option = ''
        try:
            option = int(input("please make a choice >>"))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
            system('cls')
            cusOption()
           
        elif option == 2:
            system('cls')
            option2()

        elif option == 3:
            system('cls')
            option3()
        elif option == 4:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')


