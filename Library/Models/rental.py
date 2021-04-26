from Library import db

class RentalModel(db.Model):
    __tablename__ = "rentals"
    rental_id = db.Column(db.Integer, primary_key=True)
    price_day = db.Column(db.Integer, nullable=False)
    fine_day = db.Column(db.Integer, nullable=False)
    limit_day = db.Column(db.Integer, nullable=False)


    def __init__(self, price, fine, days):
       self.price_day = price
       self.fine_day = fine
       self.limit_day = days

    def __repr__(self):
        return '<Rental ID %r>' % self.rental_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def all_rentals(cls):
        def to_json(x):
            return {
                'rental_id' : x.rental_id,
                'price_day' : x.price_day,
                'fine_day' : x.fine_day,
                'limit_day' : x.limit_day
            }

        # for printing all the values of the model
        try:
            return {'Rental': list(map(lambda x: to_json(x), cls.query.all()))}
        except:
            return None
