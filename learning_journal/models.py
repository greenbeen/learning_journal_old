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

### This is where my code starts - is it even supposed to be in this file?
class Entry(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), nullable=False, unique=True) #how to require unicode and max 255 char?, how make unique? how require title? Should type be "Unicode"?
    body = Column(Unicode) #should type be Text?
    created = Column(DateTime, default=datetime.datetime.now) #what data type do I use?  Integer for date time? Datetime? DateTime?
    edited = Column(DateTime, default=datetime.datetime.now) #ditto above. How defuault to now on this and above?

    def all(self):
        return session.query(self).order_by(self.created)

    def by_id(self, id):
        return session.query(self).filter(self.id = id)
        # return session.query(self).get(id)
        

