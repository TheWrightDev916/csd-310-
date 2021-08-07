# Anthony Wright Jr - Assignment for module 9.3 - 07/28/21
#MySQL pysports update and delete

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "wright916",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}

def show_players(cursor, title):
    #INNER JOIN Query 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
 
    players = cursor.fetchall()

    print("\n  -- {} --".format(title))
    
    #loop over information and display 
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try: 

    db = mysql.connector.connect(**config) 

    cursor = db.cursor()

    #insert player and data
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")
 
    player_data = ("Smeagol", "Shire Folk", 1)

    #insert and commit
    cursor.execute(add_player, player_data)
 
    db.commit()

    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    #update
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    cursor.execute(update_player)

    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    #delete
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

    cursor.execute(delete_player)
 
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n  Press any key to continue...")

    #error
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist.")

    else:
        print(err)

finally:
    db.close()