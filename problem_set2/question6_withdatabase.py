"""
Note I know that this is outside the scope of this course however I had already 
completed this project previously and I sampled from this code for the completion
of question6 for PS2. I just wanted to include this file as well into the submission.
"""

from mysql.connector import connect

print("\nPS2 Question 6 (David Chandler Cree)")

config = {
    "user": "root",
    "password": "pass",
    "host": "localhost",
    "database": "contactbook",
}

con = connect(**config)


def which_choice(x):
    if x == "s":
        search_contact()
    elif x == "a":
        add_contact()
    elif x == "d":
        delete_contact()
    elif x == "l":
        list_contacts()
    elif x == "x":
        exit()
    else:
        print("Please choose an option from the list of choices.\n")


def return_to_menu():
    print("Action Complete!")
    print("Would you like to return to the main menu (y/N)?")
    decision = input()

    if decision == "y":
        return
    else:
        exit()


def add_contact():

    name = input("Please enter the name of the contact: ")
    addr = input("Please enter the contacts address (can be left blank): ")
    phnum = input("Please enter the contacts phone number (can be left blank): ")
    emaddr = input("Please enter the contacts email address (can be left blank): ")

    if addr == "":
        addr = "n/a"
    if phnum == "":
        phnum = "n/a"
    if emaddr == "":
        emaddr = "n/a"

    register_contact = "insert into contacts (contact_name, address, phone_number, email_address) values (%s, %s, %s, %s)"

    with con.cursor() as cursor:
        cursor.execute(register_contact, (name, addr, phnum, emaddr))
        con.commit()

    return_to_menu()


def search_contact():
    search_name = input("Please provide the name you would like to search for: ")

    print("Searching the database...")

    search_contact_book = "SELECT contact_name, address, phone_number, email_address FROM contacts WHERE contact_name = %s"

    with con.cursor() as cursor:
        cursor.execute(search_contact_book, (search_name,))
        result = cursor.fetchall()
        for row in result:
            print(row[0], "\n", row[1], "\n", row[2], "\n", row[3], "\n")

    return_to_menu()


def delete_contact():
    delete_name = input(
        "Please provide the contacts name that you would like to have deleted."
    )

    delete_contact = "DELETE FROM contacts WHERE contact_name = %s"

    confirmation = input("Are you sure you would like to delete this name (y/N)?")

    print("Deleting contact...")

    if confirmation == "y":
        with con.cursor() as cursor:
            cursor.execute(delete_contact, (delete_name,))
            con.commit()

    else:
        return

    return_to_menu()


def list_contacts():
    list_contacts = "SELECT * FROM contacts ORDER BY contact_name ASC"

    print("Searching the contact book...\n")

    print("Contact List: ")

    with con.cursor() as cursor:
        cursor.execute(list_contacts)
        result = cursor.fetchall()
        for row in result:
            print(row[0], "\n", row[1], "\n", row[2], "\n", row[3], "\n")

    return_to_menu()


if __name__ == "__main__":
    while 1:
        print("\nHello and welcome to The Contact Book.")
        print("Please select an option from the following list.")
        print("Add a new contact (a).")
        print("Search existing contacts (s).")
        print("List all contacts (l).")
        print("Delete an existing contact (d).")
        print("Exit the program (x).")
        decision = input()

        which_choice(decision)

    con.close()
