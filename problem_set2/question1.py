print("\nPS2 Question 1 (David Chandler Cree)")


def create_list(n):
    list_n = []

    i = 2

    for _ in range(0, n - 1):

        list_n.append(i)
        i += 1

    return list_n


def multiples_p(list_temp, n):
    p = 2
    enumerator = 2
    second_list = list_temp

    done = False

    while not done:
        while enumerator * p <= n:
            if enumerator * p in list_temp:
                second_list.remove(enumerator * p)

            enumerator += 1

        enumerator = 2

        if p <= n:
            p += 1
        else:
            done = True

    print("List of primes: ")
    print(second_list)

    return second_list


if __name__ == "__main__":

    n = int(input("Please enter a number for n: "))

    list_temp = create_list(n)

    primes = multiples_p(list_temp, n)

    print(f"The number of prime numbers between 1 and {n} = {len(primes)}")
