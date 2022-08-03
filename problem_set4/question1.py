
def recursive_palindrome(string):
    if len(string) < 1:
        return True
    else:
        if string[0] == string[-1]:
            return recursive_palindrome(string[1:-1])
        else:
            return False

if __name__ == "__main__":
    s = input("Please enter a string: ")
    print(s)
    ans = recursive_palindrome(s)

    print("Palindrome" if ans else "Not Palindrome")