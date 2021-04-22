from Library import db

class RentalModel(db.Model):
    __tablename__ = "rentals"
    rental_id = db.Column(db.Integer, primary_key=True)
    price_day = db.Column(db.Integer, nullable=False)
    fine_day = db.Column(db.Integer, nullable=False)
    limit_day = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Rental ID %r>' % self.rental_id
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def all_rentals(cls):
        try:
            return cls.query.all()
        except:
            return None
