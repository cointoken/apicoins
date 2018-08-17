from .models import Coins
from .models import Deposits
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime
from coins.passphrase import Passphrase

class CRUD():
    def __init__(self,engine):
        self.engine = engine
        self.session = sessionmaker(bind=engine)()


    def coins_insert(self,coins):
        if isinstance(coins,Coins):
            self.session.add(coins)
            self.session.commit()


    def coins_query_from_address(self,address_):
        if address_:
            passphrase = self.session.query(Coins.passphrase).filter_by(address=address_).first()
            return passphrase


    def coins_update(self,passphrase_,address):
        if passphrase_ and address:
            coins = self.session.query(Coins).filter_by(passphrase=passphrase_).first()
            coins.address = address
            self.session.commit()


    def deposits_insert(self,deposits):
        if isinstance(deposits,Deposits):
            self.session.add(deposits)
            self.session.commit()


    def deposits_update(self,address,txid):
        if address:
            deposits = self.session.query(Deposits).filter_by(address=address).first()
            deposits.txid = txid
            self.session.commit()


    def deposits_query_from_address(self,address):
        if address:
            txid = self.session.query(Deposits.txid).filter_by(address=address).first()
            return txid    


    def close(self):
        self.session.close()


# if __name__ == '__main__':
#     SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:toApx08@c#@localhost:3307/exchange'
#     coins = Coins('eth','0x8EDdDd51b392Ab6b090D0Fd079D5648962E29abc',Passphrase.generate(7),datetime.now())
#     engine = create_engine(SQLALCHEMY_DATABASE_URI)
#     crud = CRUD(engine)
#     crud.insert(coins)
#     crud.close()


