from datetime import date

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import ARRAY
from sqlalchemy import Boolean
from sqlalchemy import DateTime

from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Emp(Base):

  __tablename__ = "Emp"

  id             = Column("id",             Integer(),                    primary_key = True)
  name           = Column("name",           String(),                     nullable    = False)
  surname        = Column("surname",        String(),                     nullable    = False)
  contactNumbers = Column("contactNumbers", ARRAY(String),                nullable    = False)
  email          = Column("email",          String(),                     nullable    = False)
  active         = Column("active",         Boolean(),                    nullable    = False)
  insertTime     = Column("insertTime",     DateTime(timezone = False),   nullable    = False)

  def __init__(self,
               name,
               surname,
               contactNumbers,
               email):
    self.name           = name
    self.surname        = surname
    self.contactNumbers = contactNumbers
    self.email          = email

  def __repr__(self):
    return '{ id: "%s", name: "%s", surname: "%s", contactNumbers: "%s", email: "%s"}' % \
      (self.id,
       self.name,
       self.surname,
       self.contactNumbers,
       self.email)
