import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DATE,Enum,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import func

engine = create_engine("mysql+pymysql://root:123456@192.168.235.131/oldmandb",
                       encoding='utf-8',echo = False)
Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer,primary_key=True)
    name = Column(String(32), nullable=False)
    age = Column(Integer, nullable=False)
    register_date = Column(DATE, nullable=False)
    def __repr__(self):
        return "<%s name=%s>"%(self.id,self.name)

class StudyRecord(Base):
    __tablename__ = 'study_record'
    id = Column(Integer,primary_key=True)
    day = Column(Integer,nullable=False)
    status = Column(String(32),nullable=False)
    stu_id = Column(Integer,ForeignKey('student.id'))
    student = relationship("Student",backref='my_study_record')

    def __repr__(self):
            return "<%s day=%s status=%s>"%(self.student.name,self.day,self.status)
#
# class StudySchedule(Base):
#     __tablename__ = 'study_schedule'
#     id = Column(Integer, primary_key=True)
#     day = Column(Integer,nullable=False)
#     content = Column(Integer, nullable=False)
Base.metadata.create_all(engine)
Session_class = sessionmaker(bind=engine)
session = Session_class()
#
# s1 = Student(name='Alex',age=23,register_date='2019-08-21')
# s2 = Student(name='Jack',age=24,register_date='2019-08-22')
# s3 = Student(name='Rain',age=21,register_date='2019-08-23')
# s4 = Student(name='Eric',age=25,register_date='2019-08-24')
# s5 = Student(name='Tom',age=27,register_date='2019-08-25')
#
# record1 = StudyRecord(day=1,status='YES',stu_id=1)
# record2 = StudyRecord(day=2,status='NO',stu_id=1)
# record3 = StudyRecord(day=1,status='YES',stu_id=2)
# record4 = StudyRecord(day=2,status='YES',stu_id=2)
#
# session.add_all([s1,s2,s3,s4,s5,record1,record2,record3,record4])
stu_obj = session.query(Student).filter(Student.name == 'alex').first()
# print(stu_obj)
print(stu_obj.my_study_record)
session.commit()