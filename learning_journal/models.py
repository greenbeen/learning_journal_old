from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

Index('my_index', MyModel.name, unique=True, mysql_length=255)


class Entry(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False, unique=True) 
    body = Column(Unicode) 
    created = Column(DateTime, default=datetime.datetime.now) 
    edited = Column(DateTime, default=datetime.datetime.now) 

    # Need to work on how to reference session appropriately
    def all(self):
        return session.query(self).order_by(self.created)

    def by_id(self, id):
        #return session.query(self).filter(self.id = id) #this option throws an error when initializing...
        return session.query(self).get(id)


