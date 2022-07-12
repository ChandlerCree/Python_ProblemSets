import numpy as np


print("\nPS2 Question 2 (David Chandler Cree)")


def create_matrix(input_list, n):
    """np_list = np.array(temp_list)

    print(np_list)

    # print(np_list)

    print(np_list.reshape((n, n)))"""

    mat_list = []
    count = 0

    while count < n**2:

        temp_list = []

        for _ in range(0, n):
            temp_list.append(input_list[count])
            count += 1

        mat_list.append(temp_list)

    return mat_list


def is_magic(mat, n):

    sum_diagonal1 = 0
    sum_diagonal2 = 0

    for i in range(n):
        sum_diagonal1 += mat[i][i]
        sum_diagonal2 += mat[i][n - i - 1]

    if not sum_diagonal1 == sum_diagonal2:
        return False

    for i in range(n):
        sum_row = 0
        sum_col = 0

        for j in range(n):
            sum_row += mat[i][j]
            sum_col += mat[j][i]

        if not sum_row == sum_col == sum_diagonal1:
            return False

    return True


if __name__ == "__main__":

    n = int(input("Please enter the number of rows/columns for the square matrix: "))
    input_list = []

    for _ in range(0, n**2):
        value = int(
            input(
                "Please enter a number to be added to the matrix.\nNote the matrix will be constructed Left to Right.\nRow by Row.\n"
            )
        )
        input_list.append(value)

    print(f"The list you entered appears as: {input_list}")

    mat = create_matrix(input_list, n)

    print("Your matrix appears as: ")

    i = 0
    for _ in mat:
        print(mat[i])
        i += 1

    if is_magic(mat, n):
        print("The matrix you entered IS a Magic Square!")
    else:
        print("The matrix you entered IS NOT a Magic Square.")
