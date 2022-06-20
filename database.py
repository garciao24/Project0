from pickle import TRUE
import mysql.connector
import MySQLdb
import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine

import pandas as pd
import pyodbc

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

    def close(self):
        self.db.close()
