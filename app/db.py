# Sets up database
from sqlalchemy import Table, Column, Integer, String, DateTime, Boolean, ForeignKey, MetaData, create_engine
from datetime import datetime

class Db:

   def __init__(self, config):
      engineName = ''.join(['mysql+mysqlconnector://',
         config['USERNAME'], ':', config['PASSWORD'], '@',
         config['SERVER'], '/', config['SCHEMA']])
      self.engine = create_engine(engineName)
      self.set_metadata()

   def set_metadata(self):
      self.metadata = MetaData(bind=self.engine)
      self.messages = Table('msg_messages', self.metadata,
         Column('id', Integer, primary_key = True, autoincrement = True),
         Column('from', String(20), nullable = False),
         Column('to', String(20), nullable = False),
         Column('subject', String(140), nullable = False),
         Column('body', String(5000), nullable = False),
         Column('reply_to', Integer,
            ForeignKey('msg_messages.id'), nullable = True),
         Column('created', DateTime(timezone = True), nullable = False),
         Column('read', Boolean, nullable = False, default = False),
         Column('priority', String(1), nullable = False, default = 'M')
      )
      self.tags = Table('msg_tags', self.metadata,
         Column('msg_id', Integer, ForeignKey('msg_messages.id'),
            primary_key = True),
         Column('tag', String(20), nullable = False, primary_key = True)
      )
      self.metadata.create_all()

   def connect(self):
      return self.engine.connect()

## Will add methods that perform queries here

   ## Will create an insert query based on the dictionary m
   def write_message(self, m):
      try:
         conn = self.connect()
         m['created'] = datetime.today()
         if 'read' not in m:
            m['read'] = False
         result = conn.execute(self.messages.insert(), m)
         return result.inserted_primary_key[0]
      except:
         return None
