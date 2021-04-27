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

    def __repr__(self):
        return '<Book name %r>' % self.name
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def all_books(cls):
        try:
            return cls.query.all()
        except:
            return None
