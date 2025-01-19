"""
This program funntions as a library database. It stores data on books in the library and books checked out.
Both tables have commands to either, update, add, remove, print, and modify the books from the table.
Whenever an invalid input is entered, an error message will show up, indicating why an error occured.

Author: Nataly Yau

"""

class Library:
    def __init__(self):
        self.database = {'books in library':{},
                    'books checked out':{}
                    }
#ADD COMMANDS
    def add_book_to_library (self, isbn, title, author, genre, publish_year, copies):
        #Checks if book is already in the library
        if isbn not in self.database['books in library']:

            #Creates a new book for the library
            book_record = {'title': title,
                        'author': author,
                        'genre': genre,
                        'publish date': publish_year,
                        'copies': copies}
        
            #Adds the book to the library
            self.database['books in library'][isbn] = book_record
            return (f'{title} added to library with book ID {isbn}')
        else:
            return(f'Book with ISBN {isbn} already exists in the library')
    
    def check_out_book(self, isbn, checkout_id, check_out_date, due_date):
        #Checks if book is found in the library database
        if isbn in self.database['books in library']:
            book_info = self.database['books in library'][isbn]
            #Decrease the number of avaliable copies
            if book_info['copies'] > 0:
                book_info['copies'] -= 1

                checked_out_book_record = {'title': book_info['title'],
                                           'author': book_info['author'],
                                           'copies': 1, #number of copies checked out
                                           'isbn': isbn,
                                           'check_out_date': check_out_date,
                                           'due date': due_date,}
                self.database['books checked out'][checkout_id] = checked_out_book_record

                return (f'Book with ISBN {isbn} checked out by checkout ID {checkout_id}')
            else:
                #If the number of the avaliable copies is 0
                return (f'There is no more avaliable copies with ISBN {isbn}')
        else:
            return (f'Book with ISBN {isbn} could not be found in the library database')

#REMOVE COMMANDS
    def remove_book_from_library(self,isbn):
        #Checks if the book is found in the library and removes the book if it is
        if (isbn in self.database['books in library']):
            del self.database['books in library'][isbn]
            return(f'Book with ISBN {isbn} removed from library')
        #Returns when the book is not found
        else:
            return(f'Book with ISBN {isbn} was not found in the library database')

    def check_in_book(self, isbn, checkout_id):
        #Checks if book is in the "books checked out" table, and removes the book if it is
        if (checkout_id in self.database['books checked out']):
            self.database['books checked out'].pop(checkout_id)
            self.database['books in library'][isbn]['copies'] += 1 
            return (f'Book with ISBN {isbn} was returned by checkout ID {checkout_id}')
        else:
            return(f'No checked out copies found with ISBN {isbn} and checkout ID {checkout_id}')
        
#PRINT COMMANDS
    #Prints all books in the 'books in library' table
    def print_books_in_library(self):
        for isbn, book_info in self.database['books in library'].items():
            print(f'Book ISBN {isbn}')
            for key, value in book_info.items():
                print(f'{key}: {value}')
            print(" ")
    #Prints all the books in the 'books checked out' table
    def print_checked_out_books(self):
        for checkout_id, checkout_records in self.database['books checked out'].items():
            print(f'Checkout ID: {checkout_id}')
            for key, value in checkout_records.items():
                    print(f'{key}: {value}')
            print(" ")

    #Prints one book in the 'books in library table' which is identified throught the isbn
    def print_one_book_in_library(self, isbn):
        if isbn in self.database['books in library']:
            book_info = self.database['books in library'][isbn]
            print(f'Book ISBN {isbn}')
            for key, value in book_info.items():
                print(f'{key}: {value}')
        else:
            print(f'Book with ISBN {isbn} not found in the library.')

#MODIFY COMMANDS
    def add_copies_to_library(self,isbn,copies_added):
        if isbn in self.database['books in library']:
            self.database['books in library'][isbn]['copies'] += copies_added
            return (f'The total amount of copies of books with ISBN number {isbn} is now {self.database['books in library'][isbn]['copies']}')
        else:
            return(f'Book with ISBN {isbn} was not found in the Library Database')
    
    def renew_book(self,checkout_id, due_date, new_due_date):
        self.database['books checked out'][checkout_id][due_date] = new_due_date
        return (f'Your new due date is {new_due_date}')

#Add books the the 'books in library' and 'books checked out' table so that it's not empty
library_1 = Library()
library_1.add_book_to_library(9780743273565, "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925, 5)
library_1.add_book_to_library(9780061120084, "To Kill a Mockingbird", "Harper Lee", "Fiction", 1960, 3)
library_1.check_out_book(9780743273565, 1, "11/11/2023", "11/21/2023")
library_1.check_out_book(9780061120084, 2, "11/11/2023", "11/21/2023")



print()
print('Enter one of the following commands: ')
print('add a book OR add')
print('check out a book OR co')
print('remove a book from the library OR remove')
print('check in a book OR ci')
print('print books in library OR pb')
print('print one book in library OR pob')
print('print checked out books OR pco')
print('add copies to library OR ac')
print('renew book OR renew')
print('quit OR q')
print()

#loop continues until the user quits
while True:
    #Try and except to catch any invalid inputs
    try:
        #Depending on the user input, the corresponding function will run
        user_input = input()
        print()
        if user_input.lower() == 'quit' or user_input.lower() == 'q':
            break
        
        #Adds a book to the library ('books in library' table)
        elif user_input.lower() == 'add a book' or user_input.lower() == 'add':
            isbn = int(input('Enter the ISBN: '))
            title = input('Enter the title of the book: ')
            author = input('Enter the author: ')
            genre = input('Enter the genre of the book: ')
            publish_date = input('Enter the publish year: ')
            copies = int(input('Enter the number of copies: '))
            print(library_1.add_book_to_library(isbn, title, author, genre, publish_date, copies))

        #Checks out a book (adds a book to the 'books check out' table)
        elif user_input.lower() == 'check out a book' or user_input == 'co':
            isbn = int(input('Enter the ISBN: '))
            checkout_id = int(input('Enter your checkout ID: '))
            check_out_date = input('Enter the check out date in mm/dd/yyyy format: ')
            due_date = input('Enter the due date in mm/dd/yyyy format: ')
            print(library_1.check_out_book(isbn, checkout_id, check_out_date, due_date))

        #Removes a specified book from the library ('books in library' table)
        elif user_input.lower() == 'remove a book from the library' or user_input.lower() == 'remove':
            isbn = int(input('Enter the ISBN: '))
            print(library_1.remove_book_from_library(isbn))

        #Removes the specified book from the library ('books check out' table)
        elif user_input.lower() == 'check in a book' or user_input.lower() == 'ci':
            isbn = int(input('Enter the ISBN: '))
            checkout_id = int(input('Enter your checkout ID: '))
            print(library_1.check_in_book(isbn, checkout_id))

        #Prints all the books in the library ('books in library' table)
        elif user_input.lower() == 'print books in library' or user_input.lower() == 'pb':
            print(library_1.print_books_in_library())

        #Prints all books that are checked out ('books checked out' table)
        elif user_input.lower() == 'print one book in library' or user_input.lower() == 'pob':
            isbn = int(input('Enter the ISBN: '))
            print(library_1.print_one_book_in_library(isbn))

        #Prints one specified book in the Library ('books in library' table)
        elif user_input.lower() == 'print checked out books' or user_input.lower() == 'pco':
            print(library_1.print_checked_out_books())

        #Adds more copies of the specified book to the library (modifies the copies in the 'books in library' table)
        elif user_input.lower() == 'add copies to library' or user_input.lower() == 'ac':
            isbn = int(input('Enter the ISBN: '))
            copies = int(input('How many copies would you like to add: '))
            print(library_1.add_copies_to_library(isbn, copies))
            
        #Changes the due date in the 'books check out' table of a specified book
        elif user_input.lower() == 'renew book' or user_input.lower() == 'renew':
            checkout_id = int(input('Enter your checkout ID: '))
            old_due_date = input('Enter the old due date in mm/dd/yyyy format: ')
            new_due_date = input('Enter the new due date in mm/dd/yyyy format: ')
            print(library_1.renew_book(checkout_id, old_due_date, new_due_date))
       
        else:
            print('That is an invalid input')
    except Exception as e:
        print(f'Error: {str(e)}. Please try again.')
    print()
    print('Enter another command: ')   


