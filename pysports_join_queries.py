# Anthony Wright Jr - Assignment for module 9.2 - 07/27/21
# Basic Table Joins

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "wright916",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)  

    cursor = db.cursor()

    #INNER JOIN query
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    #result
    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYER RECORDS --")
    
    #loop and iterate over cursor and select query
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n  Press any key to continue... ")


    #error
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:
    db.close()