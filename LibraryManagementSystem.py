class Library:

    def __init__(self) -> None:
        self.no_of_book = 0
        self.book_list = []

    def print_no_of_books(self):
        if self.no_of_book == 0 :
            print("There is no books in the library.")
        else :
            print(f"There are {self.no_of_book} books in the library.")
            for book in self.book_list:
                print(book)
    
    def add_book(self, new_book_name):
        self.book_list.append(new_book_name)
        self.no_of_book += 1
        
def main():

    my_library = Library()

    print ("__________WellCome__To__The__Library__________\n")
    print ("Enter > Add < to add books to the library.")
    print ("Enter > Show < to show the books present the library.")

    while True:
        
        User_input = input("What you would you like to do : ").upper()

        if User_input == 'SHOW':
            my_library.print_no_of_books()

        elif User_input == 'QUIT':
            print("Exiting the library. Goodbye!")
            quit()

        elif User_input == 'ADD':
            book_name = None
            while book_name != 'BACK':
                book_name = input("Enter the book name here: ").upper()
                if book_name != 'BACK':
                    my_library.add_book(book_name)
                    print(f"Book '{book_name}' added to the library.")
                elif book_name == 'BACK':
                    break
                else :
                    print("Invalid input!")

        else :
            print("Invalid input!")

if __name__ =="__main__":
    main()
