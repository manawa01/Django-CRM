# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create dataBase
cursorObject.execute("CREATE DATABASE crmdb")

print("All Done!")