## Incubytes Consulting LLP
- Submission by - Abhishek Oli
- EDBDA
- Acts Pune

## Overview
-The logic is such that the patients data is being managed in a database managed by incubytes LLP ,
-this database has the patients data in the respective table
-a python script usses the mysql connector with XAMPP , to connect to the database
-upon connection it queries the data based on the country provided in the function
-data fetched is then pushed to respective country.csv file


## Logic Implemented
- ETL
- Database Management
- SQL CRUD Operation

**Tools & Technologies:**
- Python 
- [MySQL Workbench]https://www.mysql.com/products/workbench/
- [XAMPP Server]https://www.apachefriends.org/download.html
- [Pandas](https://pandas.pydata.org/docs/)
- [Conda Environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment)
- [MySQL connector](https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html)


## Working -

- Create Database
- Create schema and tables
- Create connector.py script that establishes connection
- Same scripts fetches data
- Exports fetched data to csv format
- Csv Naming Convention - {country}.csv
- For example - data of India will generate IND.csv


## Installation Tools
- Package Manager - pip
- pip install pandas
- pip install mysql.connector

## Future Scope
Big Data stack can be implemented for huge volume of data
input types can be changed to frontend UI using libraries like STREAMLIt using pkl file