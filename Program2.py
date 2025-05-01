# Programmer - Violet Haveman
# Date: May 1st, 2025

# Write a program that displays the data from the cities database:

# Create display cities function
import sqlite3

def displaycities(cur):
    # Print title
    print('Contents of cities.db/Cities table:')
    # Get data from cities to display
    cur.execute('SELECT * FROM Cities')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]:,.0f}')


# Execute the main function
if __name__ == '__main__':
    # Connect to the database
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()

    # Call the function
    displaycities(cur)

    # Close the connection
    conn.close()