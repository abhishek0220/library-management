from Library import db

class Reader(db.Model):
    __tablename__ = "readers"
    reader_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    charges = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return '<Reader name %r>' % self.name
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def all_readers(cls):
        try:
            return cls.query.all()
        except:
            return None
