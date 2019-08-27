import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DATE,Enum
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

engine = create_engine("mysql+pymysql://root:123456@localhost/oldboydb",
                       encoding='utf-8',echo = True)

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    passwd = Column(String(64))

    def __repr__(self):
        return "<%s name:%s>"%(self.id,self.name)

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer,primary_key=True)
    name = Column(String(32), nullable=False)
    age = Column(Integer, nullable=False)
    register_date = Column(DATE, nullable=False)
    sex = Column(Enum("M","F"), nullable=False)
    def __repr__(self):
        return "<%s name=%s>"%(self.id,self.name)
# 把继承我的儿子们都执行了 这不就是


Base.metadata.create_all(engine)


#生成了一个会话类
# Session_class = sessionmaker(bind=engine)
#生成session实例 约等于 cursor
# Session = Session_class()
# #生成你要穿件的数据对象
# user_obj = User(name='alex',passwd='alex3714')
# user_obj2 = User(name='alex',passwd='alex3714')
# user_obj3 = User(name='alex',passwd='alex3714')
#
# Session.add(user_obj)
# Session.add(user_obj2)
# Session.add(user_obj3)
#
# #只有commit之后 才会创建
#
# # data = Session.query(User).filter_by(id = 2).all()
# data = Session.query(User).filter(User.id > 1).filter(User.id < 3).first()
#
# # data = Session.query(User).filter_by(name='alex').first()
#
# print(data)
# # data.name = "jack"
# # data.passwd = 'jack3714'

# fake_user = User(name='Rain',passwd='123456')
# Session.add(fake_user)
# print(Session.query(User).filter(User.name.in_(['jack','Rain'])).all())
# Session.rollback()
# print('After Rollback')
# print(Session.query(User).filter(User.name.in_(['jack','Rain'])).count())

# print(Session.query(User.name,func.count(User.name)).group_by(User.name).all())

# s1 = Student(name='WangWei',age=23,register_date='2019-8-27',sex='M')
# Session.add(s1)
# ret = Session.query(User,Student).filter(User.id == Student.id).all()
# print(ret)
# 这种必要要有外键关联
# res = Session.query(User).join(Student).all()
# print(res)

# Session.commit()





