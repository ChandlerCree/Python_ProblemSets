import string

print("\nPS3 Question 3 (David Chandler Cree)")

def func(filename, n):

    word_count = dict()
    count = 0

    with open(filename, encoding="utf-8") as fn:
        Lines = fn.readlines()

        for line in Lines:
            line = line.translate(str.maketrans("", "", string.punctuation))
            words = line.lower().replace("\n","").split(" ")

            for w in words:
                if w != "":
                    if w in word_count:
                        word_count[w] = word_count[w] + 1

                    else:
                        word_count[w] = 1

    for key in sorted(word_count, key=word_count.get, reverse=True):
        if count < n:
            print(key, ":", word_count[key])
            count += 1
        else:
            break



if __name__ == "__main__":

    filename = "problem_set3\moby_dick.txt"

    n = int(input("Please enter a number: "))

    func(filename, n)
