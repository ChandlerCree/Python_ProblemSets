
print("\nPS3 Question 4 (David Chandler Cree)")

def kaitenzushi(n, k):
    """
    Determines which dishes will be eaten using the methodology that
    there are n dishes on the conveyorbelt and the person eating will
    only eat the dish if they haven't eaten the same dish in the last k 
    dishes that they have eaten.
    :param n: An integer signifying how many dishes will pass on the belt
    :param k: An integer signifying the number of dishes to look back at
    :return: The length of the eaten list, i.e. the number of dishes eaten
    """

    d = []
    eaten = []
    for i in range(0, n):
        temp = int(input(f"Please enter the type of dish as an integer (dish {i + 1}): "))
        d.append(temp)

    print(d)

    if len(eaten) < k:
        for dish in d[:k]:
            if dish not in eaten:
                eaten.append(dish)

    try:
        for dish in d[k:]:
            if dish not in eaten[-k:]:
                eaten.append(dish)
    except (IndexError):
        print("Error indexing the array.")

    print(f"Eaten dishes: {eaten}")

    return (len(eaten))


if __name__ == "__main__":
    n = int(input("Please enter a value for N: "))
    k = int(input("Please enter a value for K: "))

    number_eaten = kaitenzushi(n, k)

    print(f"The number of dishes eaten = {number_eaten}")

    help(kaitenzushi)

