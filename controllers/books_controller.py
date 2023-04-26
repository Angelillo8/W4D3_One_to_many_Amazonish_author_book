from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.book import Book
from models.author import Author

import repositories.book_repository as book_repo
import repositories.author_repository as author_repo

tasks_blueprint = Blueprint("books", __name__)

@tasks_blueprint.route("/books")
def books():
    books = book_repo.select_all()
    return render_template("books/index.jinja", all_books = books)

@tasks_blueprint.route("/books/new")
def new_book():
    return render_template("books/new.jinja")

@tasks_blueprint.route("/books", methods = ['POST'])
def create_book():
    title = request.form['title']
    genre = request.form['genre']
    author = request.form['author']
    new_author = Author(author)
    author_repo.save(new_author)
    book = Book(title, genre, new_author)
    book_repo.save(book)
    return redirect("/books")

@tasks_blueprint.route("/books/<id>")
def show_book(id):
    book = book_repo.select(id)
    return render_template("books/show.jinja", book=book)
    
@tasks_blueprint.route("/books/<id>/delete", methods = ['POST'])
def delete_book(id):
    book = book_repo.select(id)
    author_id = book.author.id
    author_repo.delete(author_id)
    book_repo.delete(id)
    return redirect("/books")

@tasks_blueprint.route("/books/<id>/edit")
def edit_book(id):
    book = book_repo.select(id)
    return render_template("books/edit.jinja", book=book)

@tasks_blueprint.route("/books/<id>", methods=['POST'])
def update_book(id):
    title = request.form['title']
    genre = request.form['genre']
    author_name = request.form['author']
    book = book_repo.select(id)
    author_id = book.author.id
    author = Author(author_name, author_id)
    book_updated = Book(title, genre, author, id)
    author_repo.update(author)
    book_repo.update(book_updated)
    return redirect("/books")

