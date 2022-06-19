from pickle import TRUE
import mysql.connector
import MySQLdb
import pymysql
pymysql.install_as_MySQLdb()
import os
from sqlalchemy import create_engine

import pandas as pd
import pyodbc
from collections import deque
from tabulate import tabulate

class sql:

    def __init__(self):
        self.db = pyodbc.connect("DRIVER={MySQL ODBC 8.0 ANSI Driver};SERVER=localhost;DATABASE=pizzaria;USER=root;PASSWORD=j6Av6mTSzr#6R;")##test this out 
        #self.db = mysql.connector.connect(user='root', password='j6Av6mTSzr#6R', host='127.0.0.1', database='pizzaria')
        self.cursor = self.db.cursor()

    def query(self,sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        list1 = []
        for row in result:
            list1.append(row[0])

        return list1
    
    def modify(self,sql):
        print(sql)
        self.cursor.execute(sql)
        self.cursor.commit()

    # def insert(self,sql):
    #     self.cursor.execute(sql)


    def close(self):
        self.db.close()


    # def test(self,sql):
    #     self.cursor.execute(sql)#"SELECT * FROM items"
    #     result = self.cursor.fetchall()
    #     data = deque()
    #     for row in result:
    #         data.append(row)
    #     print (tabulate(data, headers=["tt", "tttt", "ttn"]))

###################################################

# class query(sql):


#     def showCustomer(self):
#         self.cursor.execute("SELECT * FROM customer")
#         result = self.cursor.fetchall()
#         data = deque()
#         for row in result:
#             data.append(row)
#         print (tabulate(data, headers=["Customer ID", "FirstName", "LastName", "Phone", "Address"]))


#     def showItems(self):
#         self.cursor.execute("SELECT * FROM items")
#         result = self.cursor.fetchall()
#         data = deque()
#         for row in result:
#             data.append(row)
#         print (tabulate(data, headers=["Item ID", "Name", "Price", "Type", "Category"]))



#     def showOrders(self):
#         self.cursor.execute("""SELECT orders.id_orders, orders.OrderDate , customer.fname, customer.lname, items.Name, items.Price
#                             FROM pizzaria.orders 
#                             JOIN customer ON orders.id_customer = customer.id_Customer 
#                             JOIN items ON orders.id_item = items.id_item""")
#         result = self.cursor.fetchall()
#         data = deque()
#         for row in result:
#             data.append(row)
#         print (tabulate(data, headers=["ID Orders", "Order Date" , "Customer fname", "Customer lname", "Food Item" , "Price"]))


##################################################

# from misc import phone
# import csv 
# from datetime import datetime

# class insert(sql):


#     def insertCustomer(self):
#         header = ['fname', 'lname', 'phone', 'Address']

#         fname, lname = input("Enter two values: ").split()
#         phon = phone().input()
#         Address = input("Enter Address: ")

#         data = [fname, lname, phon, Address]

#         with open('./csv/customer.csv', 'w', encoding='UTF8', newline='') as f:
#             writer = csv.writer(f)

#             # write the header
#             writer.writerow(header)

#             # write the data
#             writer.writerow(data)




#     def getval(self):
#         while(True):
#             try:
#                 option = int(input("please make a choice >>"))
#             except:
#                 print('Wrong input. Please enter a number ...')
#             if option == 1:
#                 return 'Veg'
#             elif option == 2:
#                 return 'Non-Veg'
#             else:
#                 print('Invalid option. Please enter a number between 1 or 2.')


#     def insertItems(self):
#         header = ['Name','Price','Type','Category']
#         name = input("Food Name: ")
#         Price = round((int(input("Price: "))),2)
#         Type = self.getval()
#         Category = input("Category: ")

#         data = [name, Price, Type, Category]

#         with open('./csv/items.csv', 'w', encoding='UTF8', newline='') as f:
#             writer = csv.writer(f)

#             # write the header
#             writer.writerow(header)

#             # write the data
#             writer.writerow(data)



#     def insertOrder(self):
#         header = ['id_customer','id_item','OrderDate']
#         query().showCustomer()
#         numLimit = sql().query("SELECT id_Customer FROM customer ORDER BY id_Customer ASC")
#         idCust=0
#         while not int(idCust) in numLimit:
#             idCust = input("Please enter Customer ID : ")
        
#         query().showItems()
#         numLimit = sql().query("SELECT id_item FROM items ORDER BY id_item ASC")
#         itemID=0
#         while not int(itemID) in numLimit:
#             itemID = input("Please Item ID  : ")
        
#         date = datetime.today().strftime('%Y-%m-%d')


#         data = [idCust, itemID, date]

#         with open('./csv/orders.csv', 'w', encoding='UTF8', newline='') as f:
#             writer = csv.writer(f)

#             # write the header
#             writer.writerow(header)

#             # write the data
#             writer.writerow(data)



#######################################################

# class delete(sql):
#     def delCustomer(self):
#         query().showCustomer()
#         shift = 0
#         numLimit = sql().query("SELECT id_Customer FROM customer ORDER BY id_Customer ASC")
#         while not int(shift) in numLimit:
#             shift = input("Please enter ID to delete "+str(numLimit)+") : ")
#         sqlString="DELETE FROM customer WHERE id_Customer = "+shift
#         #print(sqlString)
#         sql().modify(sqlString)
#         query().showCustomer()

    
#     def delItems(self):
#         query().showItems()
#         shift = 0
#         numLimit = sql().query("SELECT id_item FROM items ORDER BY id_item ASC")
#         while not int(shift) in numLimit:
#             shift = input("Please enter ID to delete "+str(numLimit)+") : ")
#         sqlString="DELETE FROM item WHERE id_item = "+shift
#         #print(sqlString)
#         sql().modify(sqlString)
#         query().showItems()

#     def delOrders(self):#orders in progress
#         query().showOrders()
#         shift = 0
#         numLimit = sql().query("SELECT id_orders FROM orders ORDER BY id_orders ASC")
#         while not int(shift) in numLimit:
#             shift = input("Please enter ID to delete : ")
#         sqlString="DELETE FROM orders WHERE id_orders = "+shift
#         #print(sqlString)
#         sql().modify(sqlString)
#         query().showOrders()

