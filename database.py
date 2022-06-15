import mysql.connector
import MySQLdb
import pymysql
pymysql.install_as_MySQLdb()
import os





class sql:

    def __init__(self):
        self.db = mysql.connector.connect(user='root', password='j6Av6mTSzr#6R', host='127.0.0.1', database='pizzaria')
        self.cursor = self.db.cursor()

    def query(self,sql):
        self.cursor.execute(sql)#"SELECT * FROM items"
        result = self.cursor.fetchall()
        for row in result:
            print(row)
            print("\n")

    def rows(self):
        return self.cursor.rowcount

dp = sql()
#dp.query("SELECT * FROM items")
