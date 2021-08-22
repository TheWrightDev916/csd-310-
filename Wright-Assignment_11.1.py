# Anthony Wright Jr - Assignment for module 11
# 11.1 - 07/30/21
# Displays data from Bacchus Winery Tables

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "wright916",
    "host": "localhost",
    "database": "bacchus",
    "raise_on_warnings": True
}

try: 
    db = mysql.connector.connect(**config)  

    cursor = db.cursor()
 
    cursor.execute("SELECT supplier_id, on_time, delivery_delay, items_supplied FROM supplier")

    suppliers = cursor.fetchall()

    print("\n  -- DISPLAYING SUPPLIER RECORDS --")

    for supplier in suppliers: 
        print("  SUPPLIER ID        : {}\n  DELIVERY DELAY TIME: {}\n  ON TIME DELIVERY   : {}\n  ITEMS SUPPLIED     : {}\n".format(supplier[0], supplier[1], supplier[2], supplier[3]))

 
    cursor.execute("SELECT dist_id, meeting_sales, least_selling, dist_name FROM distributor")

    distributors = cursor.fetchall()

    print ("\n  -- DISPLAYING DISTRIBUTOR RECORDS --")

    for distributor in distributors:
        print("  DISTRIBUTOR ID     : {}\n  MEETING SALES QUOTA: {}\n  LEAST SELLING WINE : {}\n  NAME OF DISTRIBUTOR: {}\n".format(distributor[0], distributor[1], distributor[2], distributor[3]))
                                                                
    
    cursor.execute("SELECT employee_id, employee_name, department, hours_worked FROM employee")

    employees = cursor.fetchall()

    print("\n  -- DISPLAYING EMPLOYEE RECORDS --")

    for employee in employees: 
        print("  EMPLOYEE ID : {}\n  NAME        : {}\n  DEPARTMENT  : {}\n  HOURS WORKED: {}\n".format(employee[0], employee[1], employee[2], employee[3]))

    input("\n\nPress any key to continue... ")


  #errors
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:

    db.close()