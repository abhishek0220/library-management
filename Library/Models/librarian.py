from Library import db

class LibrarianModel(db.Model):
    __tablename__ = "librarian"
    staff_id = db.Column(db.String(120), primary_key=True)
    password = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Librarian %r>' % self.name
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def all_librarian(cls):
        try:
            return cls.query.all()
        except:
            return None
