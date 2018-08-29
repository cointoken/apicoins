
from sqlalchemy import Column,Integer,String,DateTime,DECIMAL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Coins(Base):
    __tablename__ = 'coins'
    id = Column('id',Integer,primary_key = True)
    currency = Column('currency',String(20))
    address = Column('address',String(255))
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


class Deposits(Base):
    __tablename__ = 'deposits' 
    id = Column('id',Integer,primary_key = True)
    currency = Column('currency',String(20))
    from_address = Column('from_address',String(255))
    to_address = Column('to_address',String(255))
    amount = Column('amount',DECIMAL(16,8)) 
    txid = Column('txid',String(255))
    status = Column('status',String(1))
    created_at = Column('created_at',DateTime)
    def __init__(self,currency,address,amount,created_at):
        self.currency = currency
        self.address = address
        self.amount = amount
        self.status = '0'
        self.created_at = created_at


# if __name__ == '__main__':
#     from sqlalchemy import create_engine
#     SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:toApx08@c#@localhost:3307/exchange'
#     engine = create_engine(SQLALCHEMY_DATABASE_URI)
#     Base.metadata.drop_all(engine)
#     Base.metadata.create_all(engine)

# target_metadata = db.metadata
#alembic init migrates
#alembic revision --autogenerate -m "create tables"
#alembic upgrade head

