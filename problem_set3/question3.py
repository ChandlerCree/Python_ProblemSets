import string
import math
import time

print("\nPS3 Question 3 (David Chandler Cree)")

def most_frequent(filename, n):
    """
    Takes a filepath and a number (n) and prints the n most common 
    occuring words in that file. The printed statement is structured
    in the form of a table with the left most row being the rank,
    the next row being the word, then the actual occurance, and finally
    the predicted occurance using Zipf's Law, rounded to the 1 decimal.
    Throws an exception if the file path is invalid.
    :param filename: A string to the path of a file.
    :param n: An integer determining how many words to rank
    """

    word_count = dict()
    count = 1

    try:
        print("Attempting to locate file...")
        
        with open(filename, encoding="utf-8") as fn:
            print("File Located...\nReading File...")
            time.sleep(3)
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

    except (FileNotFoundError, IOError):
        print("Invalid file path please try again.")

    a = 1
    table_data = []

    for key in sorted(word_count, key=word_count.get, reverse=True):
        if count == 1:
            C = word_count[key]

        if count <= n:
            rw = count
            logrw = math.log10(rw)
            logC = math.log10(C)

            logfw = logC - (a * logrw)

            fw = round(10 ** logfw,1)

            #Alternate way to print the information that is not structured to a table
            #print(f"{count}. {key} :   (Actual Occurance) {word_count[key]} :   (Expected Occurance) {fw}")

            table_data.append([count, key, word_count[key], fw])

            
            count += 1
        else:
            break

    for row in table_data:
        print("{: >4}. WORD: {: <8} ACTUAL OCCURANCE: {: <8} PREDICTED OCCURANCE: {: <8}".format(*row))


if __name__ == "__main__":

    filename = "problem_set3\moby_dick.txt"

    fn = input("Please enter a file path, for Moby Dick enter 'MD' by default: ")

    if fn == 'MD':
        fn = filename

    n = int(input("Please enter the number of words to rank by occurance: "))

    most_frequent(fn, n)

    help(most_frequent)

