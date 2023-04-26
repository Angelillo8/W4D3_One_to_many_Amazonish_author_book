from models.book import Book
from models.author import Author

import repositories.book_repository as book_repo
import repositories.author_repository as author_repo

# author_repo.delete_all()
# book_repo.delete_all()

# author1 = Author("Stephen King")
# author_repo.save(author1)
# author2 = Author("Miguel de Cervantes")
# author_repo.save(author2)

# book1 = Book("IT", "horror", author1)
# book_repo.save(book1)
# book2 = Book("Don Quixote", "novel", author2)
# book_repo.save(book2)

# book_repo.delete(4)

# books = book_repo.select_all()
# for book in books:
#     print(book.title)

# book_selected = book_repo.select(2)
# print(book_selected.title)
# author_repo.delete(4)

# borges = author_repo.select(6)
# borges.name = "El gran Jorge Luis Borges"
# author_repo.update(borges)

# elaleph = book_repo.select(6)
# elaleph.genre = "es un libro crema"
# book_repo.update(elaleph)