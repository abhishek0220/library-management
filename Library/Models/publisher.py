from Library import db

class Publisher(db.Model):
    __tablename__ = "publishers"
    p_id = db.Column(db.Integer, primary_key=True)
    p_name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(13), nullable=False)

    def __repr__(self):
        return '<Publisher name %r>' % self.p_name
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def all_publisher(cls):
        try:
            return cls.query.all()
        except:
            return None