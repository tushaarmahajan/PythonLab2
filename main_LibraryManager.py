from LibraryManager import LibraryManager

# Initialize the LibraryManager
library = LibraryManager()

# Sample data for 25 recently published books
books_data = [
    {"isbn": "9780134685991", "title": "Operating System Concepts", "author": "Abraham Silberschatz", "publisher": "Wiley", "volume": 10, "year": 2020, "topic": "Operating Systems"},
    {"isbn": "9780262533058", "title": "Introduction to Algorithms", "author": "Thomas H. Cormen", "publisher": "MIT Press", "volume": 3, "year": 2021, "topic": "Data Structures"},
    {"isbn": "9780134093413", "title": "Data Structures and Algorithm Analysis", "author": "Mark A. Weiss", "publisher": "Pearson", "volume": 4, "year": 2022, "topic": "Data Structures"},
    # Add more book data here...
]

# Add sample books to the library
for book in books_data:
    library.add_book(book["isbn"], book["title"], book["author"], book["publisher"], book["volume"], book["year"], book["topic"])

# Demonstrate adding a book
library.add_book("9781119454845", "Machine Learning", "Tom M. Mitchell", "McGraw Hill", 1, 2023, "Machine Learning")

# Demonstrate removing a book
library.remove_book("9781119454845")

# Demonstrate retrieving book details
print("\nBook Details:", library.get_book_details("9780134685991"))

# Demonstrate searching for books by title
print("\nSearch by Title:", library.search_books("Operating System Concepts"))

# Demonstrate searching for books by author
print("\nSearch by Author:", library.search_books("Thomas H. Cormen", search_by="author"))

# Demonstrate listing all books
print("\nList All Books:", library.list_books())

# Demonstrate updating book details
library.update_book("9780134685991", title="Operating System Concepts, 10th Edition")

# Demonstrate checking the availability of a book
print("\nCheck Availability:", library.check_availability("9780134685991"))
print("Check Availability:", library.check_availability("9781119454845"))
