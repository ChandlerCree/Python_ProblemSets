
print("\nPS3 Question 1 (David Chandler Cree)")


def perfect_number(num, print_bool):
    """
    Determines whether a number is perfect or not 
    and lists all of the proper divisors of that number
    as well as the sum of the proper divisors.
    :param num: an integer provided by the user.
    :param print_bool: a boolean to determine if the print statements should be shown
    :return: True if number is a perfect number, False if not
    """

    sum_divisors = 0

    for i in range(1, int(num / 2) + 1):
        if num % i == 0:
            sum_divisors += i
            if print_bool:
                print(f"{i} is a proper divisor of {num}.")

    if print_bool:
        print(f"\nThe sum of the divisors of {num} = {sum_divisors}.")

    if sum_divisors == num:
        if print_bool:
            print(f"Therefore {num} is a perfect number.\n")
        return True
    else:
        if print_bool:
            print(f"Unfortunately {num} is not a perfect number.\n")
        return False
    

def all_perfect(num):
    """
    Lists all the perfect numbers that are less than the provided number.
    :param num: an interger provided by the user
    """

    list_perfect = []

    for i in range(1, num):
        if perfect_number(i, False):
            list_perfect.append(i)

    print(f"The list of perfect numbers less than {num} is {list_perfect}\n")


if __name__ == "__main__":
    num = int(input("Please enter a number: "))
    perfect_number(num, True)
    all_perfect(num)

    help(perfect_number)
    help(all_perfect)