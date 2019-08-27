from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DATE,Enum,ForeignKey,Table
from sqlalchemy.orm import sessionmaker,relationship

engine = create_engine("mysql+pymysql://root:123456@192.168.235.131/oldmandb?charset=utf8",
                       encoding='utf-8',echo = False)
Base = declarative_base()

#ORM自动帮我配置维护
book_m2m_author = Table('book_m2m_author',Base.metadata,
                         Column('book_id', Integer, ForeignKey('books.id')),
                         Column('author_id', Integer, ForeignKey('authors.id')))

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    authors = relationship('Author',secondary=book_m2m_author,backref='books')

    def __repr__(self):
        return self.name
    pass

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    def __repr__(self):
        return self.name
    pass

Base.metadata.create_all(engine)