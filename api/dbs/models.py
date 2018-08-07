
from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Coins(Base):
    __tablename__ = 'coins'
    id = Column('id',Integer,primary_key = True)
    currency = Column('currency',String(20))
    address = Column('address',String(255)，unique = True)
    passphrase = Column('passphrase',String(255))
    created_at = Column('created_at',DateTime)
    def __init__(self,currency,address,passphrase,created_at):
        self.currency = currency
        self.address = address
        self.passphrase = passphrase
        self.created_at = created_at
    

    def __repr_(self):
        return '<address %r>' % self.address


    def __str__(self):
        return '<currency %r>' % self.currency


# if __name__ == '__main__':
#     from sqlalchemy import create_engine
#     from ..config import SQLALCHEMY_DATABASE_URI 
#     engine = create_engine(SQLALCHEMY_DATABASE_URI)
#     Base.metadata.drop_all(engine)
#     Base.metadata.create_all(engine)
