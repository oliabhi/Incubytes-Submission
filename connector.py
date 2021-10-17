"""
Importing necessary libraries
"""
import mysql.connector
import pandas as pd

"""
DB Used : mySql Server
Below snippet connects to localhost 

"""
database = mysql.connector.connect(
    host="localhost",
    user="root",
    database="IncubyteHospital")
cursor = database.cursor()
query2 = "select * from patients"

"""
Initiating cursor 
"""
cursor.execute(query2)

"""
Fetching rows from tables

"""
table_rows = cursor.fetchall()
df = pd.read_sql('SELECT * FROM patients', con=database)  # fitting into pandas dataframe
df.set_index(['cust_ID'], inplace=True)  # setting default index
# print (df)
ans = df.loc[df['Country'] == "IND"]