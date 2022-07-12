
print("\nPS1 Question 5 (David Chandler Cree)")


def valid_password(pw):
    num_AZ = 0
    num_az = 0
    num_09 = 0
    num_spchar = 0

    for element in pw:
        if ord(element) <= 90 and ord(element) >= 65:
            num_AZ += 1
        elif ord(element) <= 122 and ord(element) >= 97:
            num_az += 1
        elif ord(element) <= 57 and ord(element) >= 48:
            num_09 += 1
        elif (ord(element) <= 37 and ord(element) >= 35) or ord(element) == 64 or ord(element) == 33:
            num_spchar += 1
        else:
            pass

    validity = True

    print("Number of A-Z: ", num_AZ, "\nNumber of a-z: ", num_az, "\nNumber of 0-9: ", num_09,"\nNumber of !$#@%: ", num_spchar)
    print("Length of password {}".format(len(pw)))

    if num_AZ < 1 or num_az < 1 or num_09 < 1 or num_spchar < 1:
        validity = False

    if len(pw) < 6 or len(pw) > 16:
        validity = False

    return validity




if __name__ == "__main__":
    print("Please enter a password.")
    print("The password must follow these 5 rules.")
    print("1. At least one uppercase letter (A-Z) and one lowercase letter (a-z)")
    print("2. At least one digit (0-9)")
    print("3. At least one special character from !$#@%")
    print("4. Minimum length 6 characters")
    print("5. Maximum length 16 characters")
    password = input("")

    print("detemining if password is valid...")
    validity = valid_password(password)

    if validity:
        print("Your password is valid!")
    else:
        print("Your password is invalid.")