from datetime import date

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Numeric, String, Date
from sqlalchemy.orm import sessionmaker

import psycopg2

Base = declarative_base()

class Emp(Base):

  __tablename__ = "Emp"

  id   = Column("id",   Integer,    primary_key = True)
  name = Column("name", String(32), nullable    = False)
  dob  = Column("dob",  Date,       nullable    = False)
  sal  = Column("sal",  Numeric,    nullable    = False)

  def __init__(self, name, dob, sal):
    self.name = name
    self.dob  = dob
    self.sal  = sal

  def __repr__(self):
    return "{ id: '%s', name: '%s', dob: '%s', sal: '%s'}" % (self.id, self.name, self.dob, self.sal)


#engine      = create_engine("sqlite:///:memory:", case_sensitive = True, convert_unicode = False, echo = True, encoding = "utf-8")
engine      = create_engine("postgres://ejhoiybt:qqOl4yIEO4DTDLmniwf1U99aUXcMcV9x@lallah.db.elephantsql.com:5432/ejhoiybt")
metadata    = MetaData(engine)

Table("Emp", metadata, 
  Column("id",   Integer,    primary_key = True),
  Column("name", String(32), nullable    = False),
  Column("dob",  Date,       nullable    = False),
  Column("sal",  Numeric,    nullable    = False))

metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()

try:
  emp = Emp(name = "Ram", dob = date(1985, 8, 31), sal = 123.45)
  session.add(emp)
  session.commit()
except SQLAlchemyError as error:
  print(error)
finally:
  session.close()

session = Session()
emp = Emp(name = 'Sam', dob = date(1985, 8, 31), sal = 123.45)
session.add(emp)
session.commit()

emp_records = session.query(Emp).all()

for emp in emp_records:
  print(emp)
  print(emp.id, emp.name, emp.dob, emp.sal)

record = session.query(Emp).filter_by(id = 1).one()
print(record)

record = session.query(Emp).filter_by(name = "Ram").one()
session.delete(record)

session.close()
