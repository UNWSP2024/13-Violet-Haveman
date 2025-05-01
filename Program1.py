    # Programmer - Violet Haveman
    # Date: May 1st, 2025

import sqlite3


def main():
    # Connect to the database.
    conn = sqlite3.connect('cities.db')

    # Get a database cursor.
    cur = conn.cursor()

    # Add the Cities table.
    add_cities_table(cur)

    # Add rows to the Cities table.
    add_cities(cur)

    # Commit the changes.
    conn.commit()

    # Close the connection.
    conn.close()


# The add_cities_table adds the Cities table to the database.
def add_cities_table(cur):
    # If the table already exists, drop it.
    cur.execute('DROP TABLE IF EXISTS Cities')

    # Create the table.
    cur.execute('''CREATE TABLE Cities (CityID INTEGER PRIMARY KEY NOT NULL,
                                        CityName TEXT,
                                        Population REAL)''')


# The add_cities function adds 20 rows to the Cities table.
def add_cities(cur):
    cities_pop = [(1, 'Seoul', 9900000),
                  (2, 'Lima', 11000123),
                  (3, 'Tehran', 1028378),
                  (4, 'Bogotá', 3227392),
                  (5, 'Santiago', 7239183),
                  (6, 'Mexico City', 20998543),
                  (7, 'Beijing', 41238261),
                  (8, 'Baghdad', 183619),
                  (9, 'Cairo', 1383527),
                  (10, 'New York', 20003725),
                  (11, 'Toronto', 1123214),
                  (12, 'Chicago', 94029371),
                  (13, 'Buenos Aires', 15180176),
                  (14, 'Madrid', 11124311),
                  (15, 'Melbourne', 5321927),
                  (16, 'Barcelona', 12331938),
                  (17, 'Lagos', 11391329),
                  (18, 'Munich', 1827340),
                  (19, 'São Paulo', 22000000),
                  (20, 'Kuala Lumpur', 861028361)]

    for row in cities_pop:
        cur.execute('''INSERT INTO Cities (CityID, CityName, Population)
                       VALUES (?, ?, ?)''', (row[0], row[1], row[2]))


