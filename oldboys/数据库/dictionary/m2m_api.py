
from sqlalchemy.orm import sessionmaker
import creTable

Session_class = sessionmaker(bind=creTable.engine)
session = Session_class()

# b1 = creTable.Book(name = 'Python With Alex',pub_date='2014-05-02')
b2 = creTable.Book(name = 'C++ 网络编程',pub_date='2014-05-02')
# b3 = creTable.Book(name = 'PHP With Alex',pub_date='2014-05-02')
#
# a1 = creTable.Author(name = 'Alex')
a2 = creTable.Author(name = 'Jack')
a3 = creTable.Author(name = 'Rain')
#
# b1.authors = [a1,a3]
b2.authors = [a2,a3]
# b3.authors = [a1,a2,a3]
# session.add_all([b1,b2,b3,a1,a2,a3])

session.add(b2)
author_obj = session.query(creTable.Author).filter(creTable.Author.name == 'jack').first()
print(author_obj)
book_obj = session.query(creTable.Book).filter(creTable.Book.id == 5).first()
print(book_obj.authors)
# book_obj.authors.remove(author_obj)
session.commit()