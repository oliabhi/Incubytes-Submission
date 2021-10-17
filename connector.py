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
ans = df.loc[df['Country'] == "IND"]

"""
Function show_data :
parameter : country 
return : country specific data present in table
"""


def show_data(country):
    data = df.loc[df['Country'] == country]
    print(data)
