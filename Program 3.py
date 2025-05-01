# Programmer - Violet Haveman
# Date: May 1st, 2025
import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('phone_numbers.db')

    # Get a database cursor.
    cur = conn.cursor()

    # Add the Cities table.
    add_phone_table(cur)

    # Add rows to the Cities table.
    add_phone_numbers(cur)

    # Commit the changes.
    conn.commit()

    # Close the connection.
    conn.close()

# The add_phone_table adds the Cities table to the database.
def add_phone_table(cur):
    # If the table already exists, drop it.
    cur.execute('DROP TABLE IF EXISTS Cities')

    # Create the table.
    cur.execute('''CREATE TABLE Cities (NumberID INTEGER PRIMARY KEY NOT NULL,
                                        Name TEXT,
                                        PhoneNumber REAL)''')

def add_phone_numbers(cur):
    phone_numbers = [
        (1, 'Janis Johnson', 6123817182),
        (2, 'Brandon Sander', 5142761972),
        (3, 'Smelly Mcsmellerson', 1289392987),
        (4, 'Rancid Man', 3124321234),
        (5, 'Santiago Bolonga', 7231356789),
        (6, 'Melissa Bug', 209989090),
        (7, 'Benny Blanco', 4123826121),
        (8, 'Barney Lime', 1836197612),
        (9, 'Carrie Johnson', 1383527234),
        (10, 'Nellie West', 2000372512),
        (11, 'Tommy Cools', 1123214123),
        (12, 'Cinna Williams', 940293712),
        (13, 'Beatrice Yams', 1518017687),
        (14, 'Maddie Jamison', 1112431111),
        (15, 'Mackenzie Moore', 5321927234),
        (16, 'Benjamin Wesley', 1233193838),
        (17, 'Lorelai Gilmore', 1139132923),
        (18, 'Michael Thanich', 1827340123),
        (19, 'Sammy Richter', 2203209872),
        (20, 'Kamala Yarnis', 8610288627)
    ]

    for row in phone_numbers:
        cur.execute('''INSERT INTO Cities (NumberID, Name, PhoneNumber)
                       VALUES (?, ?, ?)''', (row[0], row[1], row[2]))

if __name__ == "__main__":
    main()
