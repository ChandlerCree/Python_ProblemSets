from itertools import permutations

def generate_passwords(chr_str, length):
    for i in range(1, length+1):
        yield from map("".join, permutations(chr_str,i))

chr_str = input("Please enter a string to generate passwords from: ")
length = int(input("Please enter the max length of the password: "))

print(list(generate_passwords(chr_str, length)))