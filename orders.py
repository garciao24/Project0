from database import sql


class orders():
    def addOrder(self,customer,item,date):
        pass


import pandas as pd
import pyodbc

# Import CSV
data = pd.read_csv (r'C:\Users\Ron\Desktop\Test\products.csv')   
df = pd.DataFrame(data)

# Insert DataFrame to Table
class insert(sql):
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

    # cursor.execute('''
    #             INSERT INTO products (product_id, product_name, price)
    #             VALUES (?,?,?)
    #             ''',
    #             row.product_id, 
    #             row.product_name,
    #             row.price
    #             )
    dp.commit()




# import pandas as pd

# data = pd.read_csv (r'C:\Users\wolf1\Documents\GitHub\Project0\csv\addresses.csv')   
# df = pd.DataFrame(data)

# print(df)