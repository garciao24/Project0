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
        self.cursor.execute(sql)#"SELECT * FROM items"
        result = self.cursor.fetchall()
        for row in result:
            print(row)
            print("\n")
    
    def modify(self,sql):
        pass

    def close(self):
        self.db.close()


    def test(self,sql):
        self.cursor.execute(sql)#"SELECT * FROM items"
        result = self.cursor.fetchall()
        data = deque()
        for row in result:
            data.append(row)
        print (tabulate(data, headers=["tt", "tttt", "ttn"]))



class query(sql):


    def showCustomer(self):
        self.cursor.execute("SELECT * FROM customer")
        result = self.cursor.fetchall()
        data = deque()
        for row in result:
            data.append(row)
        print (tabulate(data, headers=["Customer ID", "FirstName", "LastName", "Phone", "Address"]))


    def showItems(self):
        self.cursor.execute("SELECT * FROM items")
        result = self.cursor.fetchall()
        data = deque()
        for row in result:
            data.append(row)
        print (tabulate(data, headers=["Item ID", "Name", "Price", "Type", "Category"]))



    def showOrders(self):
        self.cursor.execute("SELECT * FROM orders")
        result = self.cursor.fetchall()
        data = deque()
        for row in result:
            data.append(row)
        print (tabulate(data, headers=["Item ID", "Name", "Price", "Type", "Category"]))