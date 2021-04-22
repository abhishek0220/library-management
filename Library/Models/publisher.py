from Library import db

class PublisherModel(db.Model):
    __tablename__ = "publishers"
    p_id = db.Column(db.Integer, primary_key=True)
    p_name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(13), nullable=False)

    def __init__(self,name,address, phone):
       self.p_name = name
       self.address = address
       self.phone = phone

    def __repr__(self):
        return '<Publisher name %r>' % self.p_name
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def all_publisher(cls):
        def to_json(x):
            return {
                'p_id' : x.p_id,
                'p_name' : x.p_name,
                'address' : x.address,
                'phone' : x.phone 
            }
        try:
            return {'publishers': list(map(lambda x: to_json(x), cls.query.all()))}
        except:
            return None