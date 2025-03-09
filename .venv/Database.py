import sqlite3
from dataclasses import dataclass
from datetime import date

@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    status: str = "available"

@dataclass
class Reader:
    id: int
    name: str
    age: int

class Library:
    def __init__(self, db_name="library.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                year INTEGER,
                status TEXT CHECK("status" IN ('available', 'borrowed'))
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS readers (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS borrowed_books (
                reader_id INTEGER,
                book_id INTEGER,
                borrow_date TEXT,
                FOREIGN KEY (reader_id) REFERENCES readers(id),
                FOREIGN KEY (book_id) REFERENCES books(id)
            )
        """)
        self.conn.commit()

    def add_book(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.cursor.execute("INSERT INTO books (title, author, year, status) VALUES (?, ?, ?, ?)",
                            (title, author, year, "available"))
        self.conn.commit()
        return self.cursor.lastrowid

    def add_reader(self, name, age):
        self.cursor.execute("INSERT INTO readers (name, age) VALUES (?, ?)",
                            (name, age))
        self.conn.commit()
        return self.cursor.lastrowid

    def borrow_book(self, reader_id, book_id):
        self.cursor.execute("SELECT status FROM books WHERE id = ?", (book_id,))
        result = self.cursor.fetchone()
        if result and result[0] == "available":
            borrow_date = date.today().strftime("%Y-%m-%d")
            self.cursor.execute("INSERT INTO borrowed_books (reader_id, book_id, borrow_date) VALUES (?, ?, ?)",
                                (reader_id, book_id, borrow_date))
            self.cursor.execute("UPDATE books SET status = 'borrowed' WHERE id = ?", (book_id,))
            self.conn.commit()
            return True
        else:
            return False

    def return_book(self, book_id):
        self.cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        book = self.cursor.fetchone()

        if book and book[0] == "borrowed":
            self.cursor.execute("UPDATE books SET status = 'available' WHERE id = ?", (book_id,))
            self.cursor.execute("DELETE FROM borrowed_books WHERE book_id = ?", (book_id,))
            self.conn.commit()
            return True
        else:
            return False

    def search_books(self, keyword):
        self.cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?",
                            ('%' + keyword + '%', '%' + keyword + '%'))
        rows = self.cursor.fetchall()
        books = [Book(id=row[0], title=row[1], author=row[2], year=[3], status=row[4]) for row in rows]
        return books

    def get_borrowed_books(self):
        self.cursor.execute("""
            SELECT books.title, books.author, readers.name, borrowed_books.borrow_date
            FROM borrowed_books
            INNER JOIN books ON borrowed_books.book_id = books.id
            INNER JOIN readers ON borrowed_books.reader_id = readers.id
        """)
        rows = self.cursor.fetchall()
        return rows

    def get_statistics(self):
        self.cursor.execute("SELECT COUNT(*) FROM books WHERE status = 'available'")
        available_count = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT COUNT(*) FROM books WHERE status = 'borrowed'")
        borrowed_count = self.cursor.fetchone()[0]

        return available_count, borrowed_count

    def __del__(self):
        self.conn.close()

if __name__ == '__main__':
    lib = Library()

    book1_id = lib.add_book("Pride and Prejudice", "Jane Austen", 1813)
    book2_id = lib.add_book("1984", "George Orwell", 1949)
    book3_id = lib.add_book("The Picture of Dorian Gray", "Oscar Wilde", 1890)
    book4_id = lib.add_book("War and Peace", "Leo Tolstoy", 1869)

    reader1_id = lib.add_reader("Ann", 24)
    reader2_id = lib.add_reader("Tom", 65)
    reader3_id = lib.add_reader("Alice", 15)

    if lib.borrow_book(reader1_id, book1_id):
        print(f"The book '{lib.search_books('Pride')[0].title}' was given to the reader.")
    else:
        print("The book is not available.")

    found_books = lib.search_books("1984")
    if found_books:
       print(f"Books found om request '1984':")
       for book in found_books:
           print(f"- {book.title} by {book.author} ({book.year})")

    borrowed_books = lib.get_borrowed_books()
    print("\nBorrowed books:")
    if borrowed_books:
       for title, author, reader_name, borrow_date in borrowed_books:
           print(f"- {title} by {author} (выдана {reader_name} {borrow_date})")
    else:
       print("No books borrowed.")

    if lib.return_book(book1_id):
       print(f"The book '{lib.search_books('Pride')[0].title}' is returned to the library.")
    else:
       print("Failed to return the book.")

    available_count, borrowed_count = lib.get_statistics()
    print(f"\nStatistics:")
    print(f"Books available: {available_count}")
    print(f"Books borrowed: {borrowed_count}")



