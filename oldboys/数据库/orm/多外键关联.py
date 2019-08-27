from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DATE,Enum,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship

engine = create_engine("mysql+pymysql://root:123456@192.168.235.131/oldmandb",
                       encoding='utf-8',echo = False)
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    billing_address_id = Column(Integer,ForeignKey("address.id"))
    shipping_address_id = Column(Integer,ForeignKey("address.id"))
    
    billing_address = relationship('Address')
    shipping_address = relationship('Address')
    pass


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer,primary_key=True)
    street = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))
    
    pass


Base.metadata.create_all(engine)