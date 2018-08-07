from .models import Coins
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime
from coins.passphrase import Passphrase

class CRUD():
    def __init__(self,engine):
        self.engine = engine
        self.session = sessionmaker(bind=engine)()


    def insert(self,coins):
        if isinstance(coins,Coins):
            self.session.add(coins)
            self.session.commit()


    def query_from_address(self,address_):
        if address_:
            passphrase = self.session.query(Coins.passphrase).filter_by(address=address_).first()
            return passphrase


    def update(self,passphrase_,address):
        if passphrase_:
            coins = self.session.query(Coins).filter_by(passphrase=passphrase_).first()
            coins.address = address
            self.session.commit()

    
    def close(self):
        self.session.close()


# if __name__ == '__main__':
#     SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:toApx08@c#@localhost:3307/exchange'
#     coins = Coins('eth','0x8EDdDd51b392Ab6b090D0Fd079D5648962E29abc',Passphrase.generate(7),datetime.now())
#     engine = create_engine(SQLALCHEMY_DATABASE_URI)
#     crud = CRUD(engine)
#     crud.insert(coins)
#     crud.close()


