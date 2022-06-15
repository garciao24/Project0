import mysql.connector
import MySQLdb
import pymysql
pymysql.install_as_MySQLdb()
import os
import pandas as pd
from sqlalchemy import create_engine





# engine = create_engine('mysql+mysqldb://%s:%s@localhost:%i/%s'
#                        %('root', 'j6Av6mTSzr#6R','127.0.0.1', 'pizzaria'))
# sql = "SELECT * FROM items;"
# df = pd.read_sql_query(sql, engine).set_index('id')
# df.head()


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

    def close(self):
        self.db.close()

dp = sql()
dp.query("SELECT * FROM items")