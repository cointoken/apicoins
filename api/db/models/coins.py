
class Coins(db.Model):
    __tablename__ = 'coins'
    id = db.Column(db.Integer,primary_key = True)
    currency = db.Column(db.String(20),nullable = False)
    address = db.Column(db.String(255),nullable = False)
    passphrase = db.Column(db.String(255),nullable = False)
    created_at = db.Column(db.DateTime)
