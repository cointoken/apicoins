
from sqlalchemy import Column,Integer,String,DateTime,DECIMAL,Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

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
    deposit_id = Column('deposit_id',Integer,unique=True,nullable=False)
    email = Column('email',String(30))
    phone_number = Column('phone_number',String(20))
    currency = Column('currency',String(20))
    from_address = Column('from_address',String(255))
    to_address = Column('to_address',String(255))
    amount = Column('amount',DECIMAL(16,8)) 
    fee = Column('fee',DECIMAL(16,8))
    txid = Column('txid',String(255))
    status = Column(Boolean)
    deposit_time = Column('deposit_time',DateTime)
    created_at = Column('created_at',DateTime)
    def __init__(self,deposit_id,currency,email,phone_number,amount,fee,from_address,deposit_time):
        self.deposit_id = deposit_id
        self.email = email
        self.phone_number = phone_number
        self.currency = currency
        self.from_address = from_address
        self.to_address = ''
        self.amount = amount
        self.fee = fee
        self.status = False
        self.deposit_time = deposit_time
        self.created_at = datetime.now()



# target_metadata = db.metadata
#alembic init migrates
#alembic revision --autogenerate -m "create tables"
#alembic upgrade head

