"""
Note that this program is written to display the first non repeated char
regardless of case. Using the lower() function I changed every character in
the string to a lowercase. Therefore if the name had only 1 capital letter
but it had a lowercase letter of the same character then it wouldn't chose
the capital.
"""

print("\nPS2 Question 4 (David Chandler Cree)")


def first_nondupe(usr_str):

    str_list = []

    for each in usr_str:
        if each not in str_list:
            str_list.append(each.lower())
        else:
            str_list.remove(each.lower())

    print(f"The first non-repeated character is: {str_list[0]}")


if __name__ == "__main__":
    usr_str = input("Please enter a string: ")

    first_nondupe(usr_str)
