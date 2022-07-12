print("\nPS2 Question 3 (David Chandler Cree)")

""" A """

print("\n(a)")

list_six = []

for x in range(1, 1001):
    list_temp = [int(n) for n in str(x)]
    if 6 in list_temp:
        list_six.append(x)

print(list_six)

""" B """

print("\n(b)")

user_str = input("Please enter your string!\n")

str_list = [n for n in user_str]

print(str_list)

spaces = 0

for each in str_list:
    if each == " ":
        spaces += 1

print(f"You have {spaces} spaces in your string.")

""" C """

print("\n(c)")

init_mat = [[1, 2], [3, 4], [5, 6]]

result_mat = [[0, 0, 0], [0, 0, 0]]

for i in range(len(init_mat)):
    for j in range(len(init_mat[0])):
        result_mat[j][i] = init_mat[i][j]

print(f"Matrix A: ")

for i in init_mat:
    print(i)

print("Matrix A(transpose): ")

for i in result_mat:
    print(i)
