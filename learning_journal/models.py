import datetime
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    Unicode,
    UnicodeText
    )

import sqlalchemy as sa

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
    body = Column(UnicodeText, default=u'') 
    created = Column(DateTime, default=datetime.datetime.utcnow) 
    edited = Column(DateTime, default=datetime.datetime.utcnow) 

    # Need to work on how to reference session appropriately
    @classmethod
    def all(cls):
        return DBSession.query(cls).order_by(sa.desc(cls.created)).all()

        # return session.query(self).order_by(self.created)
    @classmethod
    def by_id(self, id):
        #return session.query(self).filter(self.id = id) #this option throws an error when initializing...
        return DBsession.query(cls).get(id)


