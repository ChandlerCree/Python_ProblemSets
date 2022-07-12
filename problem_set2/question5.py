print("\nPS2 Question 5 (David Chandler Cree)")


def common_elem(l1, l2):
    dupes = []

    for each in l1:
        if each in l2:
            dupes.append(each)

    return dupes


if __name__ == "__main__":

    list_1 = []
    list_2 = []

    str_1 = input("Please enter your first list of numbers (separated by spaces): ")
    str_2 = input("Please enter your second list of numbers (separated by spaces): ")

    list_1 = str_1.split()
    list_2 = str_2.split()

    dupes = common_elem(list_1, list_2)

    print(
        f"Your 1st list:    {list_1}\nYour 2nd list:    {list_2}\nDuplicates list:  {dupes}"
    )
