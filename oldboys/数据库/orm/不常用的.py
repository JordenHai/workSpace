from sqlalchemy import Table,MetaData,Column,Integer,String,ForeignKey
from sqlalchemy.orm import mapper

metadata = MetaData()

user = Table(
    'user',metadata,
    Column('id',Integer,primary_key=True),
    Column('name',String(50)),
    Column('fullname',String(50)),
    Column('passwd',String(50))
)

class User(object):
    def __init__(self,name,fullname,passwd):
        self.name = name
        self.fullname = fullname
        self.passwd = passwd


mapper(User,user)