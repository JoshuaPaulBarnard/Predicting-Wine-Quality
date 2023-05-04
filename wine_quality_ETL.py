import sqlite3
import numpy as np


#   Data sources
wine_quality_data = {
    "red wine data": "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv",
    "white wine data": "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv",
    "description": "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality.names"
}

#   Load the data
red_wine = np.genfromtxt( wine_quality_data["red wine data"], delimiter=';', skip_header = 1 )
white_wine = np.genfromtxt( wine_quality_data["white wine data"], delimiter=';', skip_header = 1 )


#   Create Indicator Variables
red_wine = np.append( red_wine, np.full( (len( red_wine ), 1), "Red Wine" ), 1 )
red_wine = np.append( red_wine, np.ones( ( len(red_wine), 1 ) ), 1 )
red_wine = np.append( red_wine, np.zeros( ( len(red_wine), 1 ) ), 1 )

white_wine = np.append( white_wine, np.full( (len(  white_wine ), 1), "White Wine" ), 1 )
white_wine = np.append( white_wine, np.zeros( ( len( white_wine ), 1 ) ), 1 )
white_wine = np.append( white_wine, np.ones( ( len( white_wine ), 1 ) ), 1 )


#   Combine the datasets
wine_quality = np.concatenate( (red_wine, white_wine) )


# Create an empty database
connection = sqlite3.connect('wine_quality.db')
cursor = connection.cursor()


# Create the table(s) in the database
sql_file = open("wine_quality.sql")
sql_as_string = sql_file.read()
cursor.executescript(sql_as_string)
sql_file.close()


# Fill the table(s) in the database
for counter_n in range( len( wine_quality ) ):
    # Insert data into the wine_quality table.
    cursor.execute( "INSERT INTO wine_quality VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )",
                           ( counter_n + 1, wine_quality[counter_n][11], wine_quality[counter_n][13],
                             wine_quality[counter_n][14], wine_quality[counter_n][12],  wine_quality[counter_n][0],
                             wine_quality[counter_n][1],  wine_quality[counter_n][2], wine_quality[counter_n][3],
                             wine_quality[counter_n][4],  wine_quality[counter_n][5], wine_quality[counter_n][6],
                             wine_quality[counter_n][7],  wine_quality[counter_n][8], wine_quality[counter_n][9],
                             wine_quality[counter_n][10]
                             ) )
    connection.commit()