class Library:

    def __init__(self,listOfBooks):
       self.books = listOfBooks

    def displayAvailableBooks(self):
       print("books present in this library are:")
       for book in self.books:
           print("*" +book)
 
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"you have been issued {bookName}. please keep it safe and return in 15 days")
            self.books.remove(bookName)
            return True
        else:
            print("sorry, this book has been issued to someone else. please wait untill yhe book is returned")
            return False


    def returnBook(self,bookName):
       self.books.append(bookName)
       print("Thanks for returning the book! hope you enjoyed reading")



      

class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow:")
        return self.book
        
    def returnBook(self):
        self.book = input("Enter the name of the book you want to return:")
        return self.book
                                                                           


if __name__ == "__main__":
    centraLibrary = Library(["Algorithims","dJango","Clrs","python notes"])
    # centraLibrary.displayAvailableBooks
    while(True):
        welcomeMsg = '''====welcome to Central Library===
        please choose an option
        1.Listing all the books
        2.Request a book
        3.Return a book
        4.Exit the library
         '''
        
        print(welcomeMsg)

        a = int(input("Enter your choice:"))
        if a==1:
             centraLibrary.displayAvailableBooks()

        elif a==2:
            centraLibrary.borrowBook(Student.requestBook())

        elif a==3:
            centraLibrary.returnBook(Student.returnBook())

        elif a==4:
            print("Thanks for using the library! Have a great day")
            exit()

        else:
            print("Inavild choice!")





