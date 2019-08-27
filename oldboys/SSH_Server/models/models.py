from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,UniqueConstraint,Table,ForeignKey
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy_utils import ChoiceType

Base = declarative_base()

user_m2m_bindhost = Table('user_m2m_bindhost',Base.metadata,
                         Column('userprofile_id', Integer, ForeignKey('user_profile.id')),
                         Column('bindhost_id', Integer, ForeignKey('bind_host.id')))

bindhost_m2m_hostgroup = Table('bindhost_m2m_hostgroup',Base.metadata,
                         Column('bindhost_id', Integer, ForeignKey('bind_host.id')),
                         Column('hostgroup_id', Integer, ForeignKey('host_group.id')))

user_m2m_hostgroup = Table('user_m2m_hostgroup',Base.metadata,
                         Column('userprofile_id', Integer, ForeignKey('user_profile.id')),
                         Column('hostgroup_id', Integer, ForeignKey('host_group.id')))

class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer,primary_key=True)
    hostname = Column(String(64),nullable=True)
    ip = Column(String(64),unique=True)
    port = Column(Integer,default=22)

    def __repr__(self):
        return self.hostname
    pass

class HostGroup(Base):
    __tablename__ = 'host_group'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(64), unique=True)
    bind_hosts =relationship("BindHost",secondary='bindhost_m2m_hostgroup',backref='host_groups')
    def __repr__(self):
        return self.hostname
    pass

class RemoteUser(Base):
    __tablename__ = 'remote_user'
    __table_args__ = (UniqueConstraint('auth_type',
                                       'username',
                                       'password',
                                        name='_user_passwd_uc'),)
    AuthTypes = [
        ('ssh-passwd', 'SSH/Password'),
        ('ssh-key', 'SSH/KEY'),]
    id = Column(Integer, primary_key=True)
    auth_type = Column(ChoiceType(AuthTypes))
    username = Column(String(32))
    password = Column(String(128))

    def __repr__(self):
        return self.username
    pass

class BindHost(Base):
    '''Bind host with different remote user,
          eg. 192.168.1.1 mysql passAbc123
          eg. 10.5.1.6    mysql pass532Dr!
          eg. 10.5.1.8    mysql pass532Dr!
          eg. 192.168.1.1 root
    '''
    __tablename__ = 'bind_host'
    id = Column(Integer,primary_key=True)

    host_id = Column(Integer, ForeignKey('host.id'))
    # group_id = Column(Integer,ForeignKey('host_group.id'))
    remoteuser_id = Column(Integer, ForeignKey('remote_user.id'))

    host = relationship('Host',backref='bind_hosts')
    # group = relationship('HostGroup',backredf='bind_hosts')
    remote_user = relationship('RemoteUser',backref='bind_hosts')
    __table_args__ = (UniqueConstraint('host_id','remoteuser_id', name='_host_group_remoteuser_uc'),)

    def __repr__(self):
        return "<BindHost(ip='%s',name='%s')>" % (self.host.ip,self.remote_user.username)

class UserProfile(Base):
    __tablename__ = 'user_profile'
    id = Column(Integer, primary_key=True)
    username = Column(String(32),unique=True)
    password = Column(String(128))
    bind_hosts = relationship('BindHost',secondary="user_m2m_bindhost",backref='use_profiles')
    host_groups = relationship("HostGroup",secondary="user_m2m_hostgroup",backref='use_profiles')
    def __repr__(self):
        return self.username
    pass

# class AuditLog(Base):
#     __tablename__ = 'audit_log'
#     id = Column(Integer, primary_key=True)
#     def __repr__(self):
#         return self.id
#     pass