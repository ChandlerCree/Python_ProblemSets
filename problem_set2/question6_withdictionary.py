"""
Note I know that utilizing a global variable is unorthodox and often considered
poor or bad practice however considering the simplicity of this project I chose
to use one.
"""

print("\nPS2 Question 6 (David Chandler Cree)")

cb = {}


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

    cb[name] = [addr, phnum, emaddr]

    return_to_menu()


def search_contact():
    search_name = input("Please provide the name you would like to search for: ")

    print("Searching the database...")

    if search_name in cb:
        addr = cb[search_name][0]
        phnum = cb[search_name][1]
        emaddr = cb[search_name][2]

    print(
        f"Name: {search_name}\nAddress: {addr}\nPhone Number: {phnum}\nEmail Address: {emaddr}"
    )

    return_to_menu()


def delete_contact():
    delete_name = input(
        "Please provide the contacts name that you would like to have deleted."
    )

    confirmation = input("Are you sure you would like to delete this name (y/N)?")

    print("Deleting contact...")

    if confirmation == "y":
        del cb[delete_name]
    else:
        return

    return_to_menu()


def list_contacts():

    print("Searching the contact book...\n")

    print("Contact List: ")

    for each in cb:
        addr = cb[each][0]
        phnum = cb[each][1]
        emaddr = cb[each][2]

        print(
            f"Name: {each}\nAddress: {addr}\nPhone Number: {phnum}\nEmail Address: {emaddr}\n"
        )

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
