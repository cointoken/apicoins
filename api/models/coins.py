
class Coins(db.Model):
    __tablename__ = 'coins'
    id = db.Column(db.Integer,primary_key = True)
    currency = db.Column(db.String(20),nullable = False)
    address = db.Column(db.String(255),nullable = False)
    passphrase = db.Column(db.String(255),nullable = False)
    created_at = db.Column(db.DateTime)
    def __init__(self,currency,address,passphrase,created_at)
        self.currency = currency
        self.address = address
        self.passphrase = passphrase
        self.created_at = created_at
