print("\nPS1 Question 2 (David Chandler Cree)")

def equilateral(h):
    spaces = h - 1

    for i in range(0, h):
        for _ in range(0,spaces):
            print(end=" ")

        spaces = spaces - 1

        for _ in range(0, i+1):
            print("* ", end="")

        print("\n")

if __name__ == "__main__":
    height = int(input("Please enter the value for h:"))

    equilateral(height)