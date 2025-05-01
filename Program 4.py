# Programmer - Violet Haveman
# Date: May 1st, 2025

import sqlite3

# Create choices
MIN_CHOICE = 1
MAX_CHOICE = 5
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
EXIT = 5

# Create mainline
def main():
    choice = 0
    while choice != EXIT:
        display_menu()
        choice = get_menu_choice()

        if choice == CREATE:
            create()
        elif choice == READ:
            read()
        elif choice == UPDATE:
            update()
        elif choice == DELETE:
            delete()
            
# Print/Display Menu
def display_menu():
    print('\n----- Phone Book Menu -----')
    print('1. Add a new phone number')
    print('2. Search for a phone number')
    print('3. Update a phone number')
    print('4. Delete a phone number')
    print('5. Exit the program')

# Create function that allows user to choose which function
def get_menu_choice():
    try:
        choice = int(input('Enter your choice: '))
    except ValueError:
        choice = 0

    while choice < MIN_CHOICE or choice > MAX_CHOICE:
        print(f'Valid choices are {MIN_CHOICE} through {MAX_CHOICE}.')
        try:
            choice = int(input('Enter your choice: '))
        except ValueError:
            choice = 0

    return choice

# Define each individual function for phone numbers

def create():
    print('Add New Phone Number')
    name = input('Name: ')
    phone = input('Phone Number: ')
    insert_row(name, phone)

def read():
    name = input('Enter a name to search for: ')
    num_found = display_item(name)
    print(f'{num_found} row(s) found.')

def update():
    read()
    selected_id = int(input('Enter the ID of the entry to update: '))
    name = input('Enter the new name: ')
    phone = input('Enter the new phone number: ')
    num_updated = update_row(selected_id, name, phone)
    print(f'{num_updated} row(s) updated.')

def delete():
    read()
    selected_id = int(input('Enter the ID of the entry to delete: '))
    sure = input('Are you sure you want to delete this entry? (y/n): ')
    if sure.lower() == 'y':
        num_deleted = delete_row(selected_id)
        print(f'{num_deleted} row(s) deleted.')

# Insert into database
def insert_row(name, phone):
    # Connect to database
    conn = None
    try:
        conn = sqlite3.connect('phone_numbers.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO Cities (Name, PhoneNumber)
                       VALUES (?, ?)''', (name, phone))
        conn.commit()
    except sqlite3.Error as err:
        print('Database Error:', err)
    finally:
        if conn:
            conn.close()

# Display items for user

def display_item(name):
    conn = None
    results = []
    try:
        conn = sqlite3.connect('phone_numbers.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Cities
                       WHERE lower(Name) == ?''', (name.lower(),))
        results = cur.fetchall()
        for row in results:
            print(f'ID: {row[0]:<3} Name: {row[1]:<20} Phone Number: {row[2]}')
    except sqlite3.Error as err:
        print('Database Error:', err)
    finally:
        if conn:
            conn.close()
    return len(results)

# Update rows according to user input

def update_row(id, name, phone):
    conn = None
    try:
        conn = sqlite3.connect('phone_numbers.db')
        cur = conn.cursor()
        cur.execute('''UPDATE Cities
                       SET Name = ?, PhoneNumber = ?
                       WHERE NumberID == ?''', (name, phone, id))
        conn.commit()
        return cur.rowcount
    except sqlite3.Error as err:
        print('Database Error:', err)
        return 0
    finally:
        if conn:
            conn.close()
# Delete rows according to user input

def delete_row(id):
    conn = None
    try:
        conn = sqlite3.connect('phone_numbers.db')
        cur = conn.cursor()
        cur.execute('''DELETE FROM Cities
                       WHERE NumberID == ?''', (id,))
        conn.commit()
        return cur.rowcount
    except sqlite3.Error as err:
        print('Database Error:', err)
        return 0
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    main()
