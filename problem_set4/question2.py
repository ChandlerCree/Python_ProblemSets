def recursive_binary(n):
    if n > 1:
        recursive_binary(n//2)
    ls.append(n % 2)
    return ls


if __name__ == "__main__":
    num = int(input("Please enter a number to be converted: "))
    ls = []

    ls = recursive_binary(num)

    ls = [str(i) for i in ls]

    print(''.join(ls))