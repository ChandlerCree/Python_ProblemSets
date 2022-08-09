import sys

class Book:
    def __init__(self):
        self.isbn = input("Please enter the ISBN: ")
        self.title = input("Please enter the Title: ")
        self.authors = []
        num_authors = None
        while num_authors == None or num_authors > 0:
            if num_authors == None:
                num_authors = int(input("Please enter the number of Authors: "))
            self.authors.append(input("Please enter an Author: "))
            num_authors -= 1
        self.publisher = input("Please enter the Publisher: ")
        self.pub_date = input("Please enter the Publication Date: ")
        self.price = float(input("Please enter the Price in US $:"))

        self.return_string = f'''
        The ISBN number for {self.title} is {self.isbn}.
        The authors of this book are: 
            {', '.join(self.authors)}
        The book was published by {self.publisher} on {self.pub_date}.
        The price of the book is ${self.price}.\n
        '''

    def __str__(self):
        return self.return_string


class Library:
    def __init__(self):
        self.book_list = {}

    def add_book(self):
        b = Book()
        print(f"\n\nAdding Book: {b.isbn}\n")
        self.book_list[b.isbn] = {
            "title": b.title,
            "authors": b.authors, 
            "publisher": b.publisher,
            "pub_date": b.pub_date,
            "price $": b.price,
            }

    def remove_book(self, isbn):
        print(f"\n\nRemoving Book: {isbn}\n")
        del self.book_list[isbn]
    
    def display_books(self):
        print("\n\nDisplay Output\n")
        for val in self.book_list:
            print(f'''
            The ISBN number for {self.book_list[val]["title"]} is {val}.
            The authors of this book are: 
                {', '.join(self.book_list[val]["authors"])}
            The book was published by {self.book_list[val]["publisher"]} on {self.book_list[val]["pub_date"]}.
            The price of the book is ${self.book_list[val]["price $"]}.
            ''')

    def search_isbn(self, isbn):
        print("\n\nSearch Output\n")
        print(f'''
            The ISBN number for {self.book_list[isbn]["title"]} is {isbn}.
            The authors of this book are: 
                {', '.join(self.book_list[isbn]["authors"])}
            The book was published by {self.book_list[isbn]["publisher"]} on {self.book_list[isbn]["pub_date"]}.
            The price of the book is ${self.book_list[isbn]["price $"]}.
            ''')

    def search_author(self, author):
        print("\n\nSearch Author\n")
        for val in self.book_list:
            if author in self.book_list[val]["authors"]:
                print(f'''
            The ISBN number for {self.book_list[val]["title"]} is {val}.
            The authors of this book are: 
                {', '.join(self.book_list[val]["authors"])}
            The book was published by {self.book_list[val]["publisher"]} on {self.book_list[val]["pub_date"]}.
            The price of the book is ${self.book_list[val]["price $"]}.
            ''')

    def search_price(self, price):
        print(f"\n\nSearch Price Lower Than: {price}\n")
        for val in self.book_list:
            if self.book_list[val]["price $"] < price:
                print(f'''
            The ISBN number for {self.book_list[val]["title"]} is {val}.
            The authors of this book are: 
                {', '.join(self.book_list[val]["authors"])}
            The book was published by {self.book_list[val]["publisher"]} on {self.book_list[val]["pub_date"]}.
            The price of the book is ${self.book_list[val]["price $"]}.
            ''')

        

if __name__ == "__main__":

    usr_inp = None
    Lib = Library()

    print("Hello and welcome to the Library!")

    while usr_inp != '0':

        print("Please select an option for what you would like to do.")
        print("To add a book 'a'.")
        print("To remove a book 'r'.")
        print("To display all books 'd'.")
        print("To search for a book by ISBN 'i'.")
        print("To search for a book by author 's'.")
        print("To search for a book by price 'p'.")
        print("To exit the program '0'.")

        usr_inp = input("Enter your selection: ")

        if usr_inp == "0":
            sys.exit()
        elif usr_inp == "a":
            Lib.add_book()
        elif usr_inp == "r":
            isbn = input("Please enter the ISBN of the book: ")
            Lib.remove_book(isbn)
        elif usr_inp == "d":
            Lib.display_books()
        elif usr_inp == "i":
            isbn = input("Please enter the ISBN of the book: ")
            Lib.search_isbn(isbn)
        elif usr_inp == "s":
            author = input("Please enter the authors name: ")
            Lib.search_author(author)
        elif usr_inp == "p":
            print("Note that this option displays all books cheaper than a given price.")
            price = int(input("Please enter the price to search by: "))
            Lib.search_price(price)
        else: 
            print("Unfortunately that is not an option...\n")
            