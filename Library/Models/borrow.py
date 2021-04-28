from Library import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class BorrowModel(db.Model):
    __tablename__ = "borrows"
    _id = db.Column(db.Integer, primary_key=True)
    p_name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(13), nullable=False)

    book_id = db.Column(db.Integer, ForeignKey('books._id'))
    reader_id = db.Column(db.Integer, ForeignKey('readers.reader_id'))

    books = relationship("BooksModel", back_populates="borrows")
    readers = relationship("ReaderModel", back_populates="borrows")

    def __init__(self, name, address, phone, _book_id, _reader_id):
       self.p_name = name
       self.address = address
       self.phone = phone
       self.book_id = _book_id
       self.reader_id = _reader_id

    def __repr__(self):
        return '<Publisher name %r>' % self.p_name

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def all_borrowers(cls):
        def to_json(x):
            return {
                'borrow_id' : x._id,
                'p_name' : x.p_name,
                'address' : x.address,
                'phone' : x.phone,
                'bookId' : x.book_id,
                'readerId' : x.reader_id
            }
        try:
            return {'borrowers': list(map(lambda x: to_json(x), cls.query.all()))}
        except:
            return None
