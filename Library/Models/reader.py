from Library import db

class ReaderModel(db.Model):
    __tablename__ = "readers"
    reader_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    charges = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, _name, _email, _charges):
       self.name = _name
       self.email = _email
       self.charges = _charges

    def __repr__(self):
        return '<Reader name %r>' % self.name

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def all_readers(cls):
        def to_json(x):
            return {
                'reader_id' : x.reader_id,
                'name' : x.name,
                'email' : x.email,
                'charges' : x.charges
            }
        try:
            return {'Reader': list(map(lambda x: to_json(x), cls.query.all()))}
        except:
            return None
