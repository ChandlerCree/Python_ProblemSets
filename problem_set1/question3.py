print("\nPS1 Question 3 (David Chandler Cree)")

def fibonacci(n):
    n1, n2 = 0, 1
    count = 0

    if n <= 0:
        print("Invalid number of terms.")
    elif n == 1:
        print(n1)
    else:
        while count < n:
            print(n1, end=" ")
            next = n1 + n2
            n1 = n2
            n2 = next
            count += 1
    


if __name__ == "__main__":
    n = int(input("Please enter a value of n: "))
    print("Fibonacci Sequence: ")

    fibonacci(n)
