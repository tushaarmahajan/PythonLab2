class LibraryManager:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, publisher, volume, year, topic):
        """Add a book to the library."""
        if isbn in self.books:
            print(f"Book with ISBN {isbn} already exists.")
            return
        self.books[isbn] = {
            "title": title,
            "author": author,
            "publisher": publisher,
            "volume": volume,
            "year": year,
            "topic": topic
        }

    def remove_book(self, isbn):
        """Remove a book from the library by its ISBN."""
        if isbn in self.books:
            del self.books[isbn]
            print(f"Book with ISBN {isbn} removed.")
        else:
            print(f"Book with ISBN {isbn} not found.")

    def get_book_details(self, isbn):
        """Retrieve and display the details of a book using its ISBN."""
        return self.books.get(isbn, "Book not found.")

    def search_books(self, query, search_by='title'):
        """Search for books by title or author."""
        if search_by not in ['title', 'author']:
            return "Invalid search criteria. Use 'title' or 'author'."
        
        results = []
        for book in self.books.values():
            if query.lower() in book[search_by].lower():
                results.append(book)
        return results

    def list_books(self):
        """List all books currently in the library."""
        return list(self.books.values())

    def update_book(self, isbn, **kwargs):
        """Update the details of an existing book."""
        if isbn not in self.books:
            print(f"Book with ISBN {isbn} not found.")
            return
        self.books[isbn].update(kwargs)
        print(f"Book with ISBN {isbn} updated.")

    def check_availability(self, isbn):
        """Check if a book is available in the library by its ISBN."""
        return isbn in self.books
