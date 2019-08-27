# _*_coding:utf-8_*_
# __author__ = 'Alex Li'

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base() #生成一个ORM 基类

class PathTag(Base):

    __tablename__ = "pathTag"
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Packet_in_times = Column(String(64))
    Dpid = Column(String(64))
    Cookie = Column(String(64))
    Source_address = Column(String(64))
    Destination_address = Column(String(64))
    Data_len = Column(String(64))

    def __repr__(self):
        return (
            "<PathTag(id='%s',packet_in='%s',dpid='%s',cookie='%s',source_address='%s',Destination_address='%s',Data_len='%s')>"
            % (
                self.Id,
                self.Packet_in_times,
                self.Dpid,
                self.Cookie,
                self.Source_address,
                self.Destination_address,
                self.Data_len,
            )
        )

