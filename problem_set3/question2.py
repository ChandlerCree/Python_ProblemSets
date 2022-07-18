
print("\nPS3 Question 2 (David Chandler Cree)")

def validate(ccn):
    """
    Validates whether or not a credit card is valid. First reverses the credit
    card number, then takes the odd-indexed digits and doubles their values. 
    If the values doubled are greater than 10 then it takes the sum of the 2 
    digits. Then sums the whole modified array and if the modulo of that summed
    array is 0 it deems the credit card number valid.
    :param ccn: An array of the 4, 4 digit sections of the credit card
    """
    reverse_ccn = ccn[::-1]
    print(f"The reversed credit card number is: {reverse_ccn}")

    ccn_list = [char for char in reverse_ccn]

    ccn_nospace = []

    for each in ccn_list:
        if each.strip():
            ccn_nospace.append(each)

    odd = False
    sum_list = []

    for element in ccn_nospace:
        if odd:
            element = int(element) * 2

            if element > 10:
                element = [char for char in str(element)]

                sum_list.append(element[0] + element[1])

            odd = False
        else:
            odd = True

    sum = 0

    for element in sum_list:
        sum += int(element)

    if sum % 10 == 0:
        print("This is a valid credit card number!")
    else:
        print("This credit card number unfortunately is invalid.")


if __name__ == "__main__":

    credit_card_number = []
    i = 0
    while i < 4:
        num = input(f"Please enter the credit card number 4 digits at a time. Group {i+1}: ")
        if len(num) == 4:
            credit_card_number.append(num)
            i += 1
        else:
            print("You must enter the number in groups of 4 digits.")

    print(f"The credit card number you entered is: {credit_card_number}")

    validate(" ".join(credit_card_number))

    help(validate)

    