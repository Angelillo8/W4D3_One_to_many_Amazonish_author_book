from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.author_repository as author_repo

def save(book):
    sql = "INSERT INTO books (title, genre, author_id) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title, book.genre, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repo.select(row['author_id'])
        book = Book(row['title'], row['genre'], author, row['id'])
        books.append(book)
    return books

def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)
    if result:
        result = result[0]
        author = author_repo.select(result['author_id'])
        book = Book(result['title'], result['genre'], author, result['id'])
    return book

def update(book):
    sql = "UPDATE books SET (title, genre, author_id) = (%s, %s, %s) WHERE id = %s"
    values = [book.title, book.genre, book.author.id, book.id]
    run_sql(sql, values)