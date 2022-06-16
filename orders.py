import pandas as pd
import pyodbc
from database import sql


# class orders():
#     def addOrder(self,customer,item,date):
#         pass



# Import CSV
data = pd.read_csv (r'C:\Users\Ron\Desktop\Test\products.csv')   
df = pd.DataFrame(data)

# Insert DataFrame to Table
class orders(sql):
    dp = sql()

    def orders():
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



class customer(sql):
    dp = sql()

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










    


# import pandas as pd

# data = pd.read_csv (r'C:\Users\wolf1\Documents\GitHub\Project0\csv\addresses.csv')   
# df = pd.DataFrame(data)

# print(df)