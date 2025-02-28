class Book():
    def __init__(self, name, author, length):
        self.name = name
        self.author = author
        self.length = length

    def introBook(self):
        return self.name + " by " + self.author
    
    def __str__(self):  
        return self.name

class TextBook(Book):
    def __init__(self, name, author, length, subject):
        super().__init__(name, author, length)
        self.subject = subject

    def introBook(self):
        return self.name + " written by " + self.author

myJavaTextbook = TextBook("Intro to Java", "John Dove", 421, "Computer Science")

class Library():
    def __init__(self, name, city, books:list, book_of_day): 
        self.name = name                                     
        self.city = city
        self.books = books
        self.book_of_day = book_of_day
    
    def updateDailyBook(self, new_book : Book):
        self.book_of_day = new_book


myCSTextbook = TextBook("C Programming Language", "Brian W. Kernighan", 217, "Computer Science")
myBook = Book("Frankenstein", "Mary Shelley", 280)
myBook2 = Book("Paradise Lost", "John Milton", 600)

myLibrary = Library("Temple City Library", "Temple City", [myCSTextbook, myBook, myBook2], myBook2)

print(myLibrary.book_of_day)
myLibrary.updateDailyBook(myCSTextbook)
print(myLibrary.book_of_day)

# Textbook is the child class of Book
# Library contains Book objects. IT DOES NOT INHERIT ANYTHING.
# Just because a class is a parent class doesn't mean you can't make an object from it.
#   See myBook and myBook2

