from Library import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class BooksModel(db.Model):
    __tablename__ = "books"
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    isbn = db.Column(db.Integer, nullable=False)
    total_copies = db.Column(db.Integer, nullable=False)
    available_copies = db.Column(db.Integer, nullable=False)
    authors = db.Column(db.String(), nullable=True)
    pages = db.Column(db.Integer, nullable=True)
    thumbnail_url = db.Column(db.String(), nullable=True)
    categories = db.Column(db.String(), nullable=True)
    short_desc = db.Column(db.String(), nullable=True)
    long_desc = db.Column(db.String(), nullable=True)

    p_id = db.Column(db.Integer, ForeignKey('publishers.p_id'))
    rental_id = db.Column(db.Integer, ForeignKey('rentals.rental_id'))

    publishers = relationship("PublisherModel", back_populates="books")
    rentals = relationship("RentalModel", back_populates="books")

    borrows = relationship("BorrowModel", back_populates="books")

    def __init__(self, _id, _name, _isbn, _total_copies, _authors, _pages, _thumbnail_url, _categories, _short_desc, _long_desc, _p_id, _rental_id):
        self._id = _id
        self.name = _name
        self.isbn = _isbn
        self.total_copies = _total_copies
        self.available_copies = _total_copies
        self.authors = _authors
        self.pages = _pages
        self.thumbnail_url = _thumbnail_url
        self.categories = _categories
        self.short_desc = _short_desc
        self.long_desc = _long_desc
        self.p_id = _p_id
        self.rental_id = _rental_id

    def __repr__(self):
        return '<Book name %r>' % self.name

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def all_books(cls, bookObj = None):
        def to_json(x):
            return {
                '_id' : x._id,
                'name' : x.name,
                'isbn' : x.isbn,
                'total_copies' : x.total_copies,
                'available_copies' : x.available_copies,
                'authors,' : x.authors,
                'pages,' : x.pages,
                'thumbnail_url,' : x.thumbnail_url,
                'categories,' : x.categories,
                'short_desc,' : x.short_desc,
                'long_desc,' : x.long_desc,
                'p_id,' : x.p_id,
                'rental_id,' : x.rental_id
            }
        if(bookObj is not None):
            return to_json(bookObj)
        try:
            return {'books': list(map(lambda x: to_json(x), cls.query.all()))}
        except:
            return None
