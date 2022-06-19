import csv
from datetime import datetime
from csvWrite import write
from database import sql
from misc import phone
from show import show

#class with functions to create csv files based on the user input


class insert(sql):


    def insertCustomer(self):
        header = ['fname', 'lname', 'phone', 'Address']

        fname, lname = input("Enter First and Last Name: ").split()
        phon = phone().input()
        Address = input("Enter Address: ")

        data = [fname, lname, phon, Address]

        with open('./csv/customer.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)

            # write the data
            writer.writerow(data)

        write().customer()


    def getval(self):
        while(True):
            try:
                print("Vegan-1")
                print("Non-Vegan")
                option = int(input("please make a choice >>"))
            except:
                print('Wrong input. Please enter a number ...')
            if option == 1:
                return 'Veg'
            elif option == 2:
                return 'Non-Veg'
            else:
                print('Invalid option. Please enter a number between 1 or 2.')


    def insertItems(self):
        header = ['Name','Price','Type','Category']
        name = input("Food Name: ")
        Price = round((float(input("Price: "))),2)
        Type = self.getval()
        Category = input("Category: ")

        data = [name, Price, Type, Category]

        with open('./csv/items.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)

            # write the data
            writer.writerow(data)

        write().items()



    def insertOrder(self):
        header = ['id_customer','id_item','OrderDate']
        show().showCustomer()
        numLimit = sql().query("SELECT id_Customer FROM customer ORDER BY id_Customer ASC")
        idCust=0
        while not int(idCust) in numLimit:
            idCust = input("Please enter Customer ID : ")
        
        show().showItems()
        numLimit = sql().query("SELECT id_item FROM items ORDER BY id_item ASC")
        itemID=0
        while not int(itemID) in numLimit:
            itemID = input("Please Item ID  : ")
        
        date = datetime.today().strftime('%Y-%m-%d')



        data = [idCust, itemID, date]

        with open('./csv/orders.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)

            # write the data
            writer.writerow(data)

        write().orders()