import pandas as pd
import pyodbc
from database import sql


#dp = sql()

#CLASS adds data from csv to mysql database
class write(sql):
    
    def orders(self):
        data = pd.read_csv (r'C:\Users\wolf1\Documents\GitHub\Project0\csv\orders.csv')   
        df = pd.DataFrame(data)
        for row in df.itertuples():
            self.cursor.execute('''
            INSERT INTO orders (id_customer, id_item, OrderDate)
            VALUES (?,?,?)
            ''',
            row.id_customer, 
            row.id_item,
            row.OrderDate
            )
        self.cursor.commit()

    def items(self):
        data = pd.read_csv (r'C:\Users\wolf1\Documents\GitHub\Project0\csv\items.csv')   
        df = pd.DataFrame(data)
        for row in df.itertuples():
            self.cursor.execute('''
            INSERT INTO items (Name, Price, Type, Category)
            VALUES (?,?,?,?)
            ''',
            row.Name, 
            row.Price,
            row.Type,
            row.Category
                 )
        self.cursor.commit()

    def customer(self):
        data = pd.read_csv (r'C:\Users\wolf1\Documents\GitHub\Project0\csv\customer.csv')   
        df = pd.DataFrame(data)
        for row in df.itertuples():
            self.cursor.execute('''
            INSERT INTO customer (fname, lname, phone, Address)
            VALUES (?,?,?,?)
            ''',
            row.fname, 
            row.lname,
            row.phone,
            row.Address
                 )
        self.cursor.commit()