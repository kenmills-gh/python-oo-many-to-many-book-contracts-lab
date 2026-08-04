class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        """Returns a list of all contracts associated with this author."""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Returns a unique list of books associated with this author through contracts."""
        books_list = []
        for contract in self.contracts():
            if contract.book not in books_list:
                books_list.append(contract.book)
        return books_list

    def sign_contract(self, book, date, royalties):
        """Creates and returns a new Contract object between the author and the specified book."""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Returns the total sum of royalties earned from all of the author's contracts."""
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        """Returns a list of all contracts associated with this book."""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Returns a unique list of authors associated with this book through contracts."""
        authors_list = []
        for contract in self.contracts():
            if contract.author not in authors_list:
                authors_list.append(contract.author)
        return authors_list


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception("Author must be an instance of the Author class.")

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception("Book must be an instance of the Book class.")

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception("Date must be a string.")

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int) and not isinstance(royalties, bool):
            self._royalties = royalties
        else:
            raise Exception("Royalties must be an integer.")

    @classmethod
    def contracts_by_date(cls, date):
        """Returns a list of all contracts that match the specified date."""
        return [contract for contract in cls.all if contract.date == date]
