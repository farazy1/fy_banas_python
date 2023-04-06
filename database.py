import sys
import math
import random
import threading
import time
import re
import sqlite3
import csv 

def print_DB():
    try:
        result = theCursor.execute("SELECT id, FName, LNAME, Age, Address, Salary, HireDate FROM Employees")
        for row in result:
            print("ID :", row[0])
            print("FName :", row[1])
            print("LName :", row[2])
            print("Age :", row[3])
            print("Address :", row[4])
            print("Salary :", row[5])
            print("HireDate :", row[6])
    except sqlite3.OperationalError:
        print("The table doesnt exist")
    except:
            print("Couldnt get data")

try:
    db_conn = sqlite3.connect('test.db')
    print("Database Created")
except sqlite3.OperationalError:
    print("Database connection not created")

try:
    theCursor = db_conn.cursor()
    print("Cursor Created")
except sqlite3.OperationalError:
    print("Cursor not created")

#PRIMARY KEY AUTOINCREMENT UNIQUE
try:
    db_conn.execute(
    '''CREATE TABLE IF NOT EXISTS Employees(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    FName TEXT NOT NULL,
    LName TEXT NOT NULL,
    Age INT NOT NULL,
    Address TEXT,
    Salary REAL,
    HireDate TEXT)''')
    db_conn.commit()
    print("Table created")
except sqlite3.OperationalError:
    print("Table Not Created")

db_conn.execute("INSERT INTO Employees ( FName, LName, Age, Address, Salary, HireDate)"
                "VALUES ('Faraz', 'Test', 100, '123 Main St', '500,000', date('now'))")
db_conn.commit()
print_DB()
db_conn.close

