import pandas as pd
import pyodbc
from database import sql


# class orders():
#     def addOrder(self,customer,item,date):
#         pass



# Import CSV
data = pd.read_csv (r'C:\Users\wolf1\Documents\GitHub\Project0\csv\customer.csv')   
df = pd.DataFrame(data)
dp = sql()
# Insert DataFrame to Table
class orders():
    
    def orders():    
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

        pass
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



# class customer(sql):
#     dp = sql()

#     for row in df.itertuples():
#         dp.query('''
#         INSERT INTO customer (fname, lname, phone, Address)
#         VALUES (?,?,?)
#                  ''',
#                  row.fname, 
#                  row.lname,
#                  row.phone,
#                  row.Address
#                  )
#     dp.commit()

# class items(sql):
#     dp = sql()
#     for row in df.itertuples():
#         dp.query('''
#         INSERT INTO orders (id_customer, id_item, OrderDate)
#         VALUES (?,?,?)
#                 ''',
#                  row.id_customer, 
#                  row.id_item,
#                  row.OrderDate
#                  )
#     dp.commit()







# act = customer()
# act()

    


# import pandas as pd

# data = pd.read_csv (r'C:\Users\wolf1\Documents\GitHub\Project0\csv\addresses.csv')   
# df = pd.DataFrame(data)


db = sql()
for row in df.itertuples():
    db.query('''
                INSERT INTO products (product_id, product_name, price)
                VALUES (?,?,?)
                ''',
                row.product_id, 
                row.product_name,
                row.price
                )
db.commit()

#print(df)