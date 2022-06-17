import pandas as pd
import pyodbc
from database import sql



dp = sql()

#CLASS adds data from csv to mysql database
class csv():
    
    def orders():
        data = pd.read_csv (r'C:\Users\wolf1\Documents\GitHub\Project0\csv\orders.csv')   
        df = pd.DataFrame(data)
        for row in df.itertuples():
            dp.query('''
            INSERT INTO orders (id_customer, id_item, OrderDate)
            VALUES (?,?,?)
            ''',
            row.id_customer, 
            row.id_item,
            row.OrderDate
            )
        dp.commit()

    def items():
        data = pd.read_csv (r'C:\Users\wolf1\Documents\GitHub\Project0\csv\items.csv')   
        df = pd.DataFrame(data)
        for row in df.itertuples():
            dp.query('''
            INSERT INTO items (Name, Price, Type, Category)
            VALUES (?,?,?,?)
            ''',
            row.Name, 
            row.Price,
            row.Type,
            row.Category
                 )
    dp.commit()

    def customer():
        data = pd.read_csv (r'C:\Users\wolf1\Documents\GitHub\Project0\csv\customer.csv')   
        df = pd.DataFrame(data)
        for row in df.itertuples():
            dp.query('''
            INSERT INTO customer (fname, lname, phone, Address)
            VALUES (?,?,?,?)
            ''',
            row.fname, 
            row.lname,
            row.phone,
            row.Address
                 )
    dp.commit()

