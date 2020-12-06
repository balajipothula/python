import sqlalchemy
import pandas

from sqlalchemy import create_engine

from sqlalchemy import inspect
from sqlalchemy.sql import text


def lambda_handler(event, context):
  
  data_frame = pandas.read_sql(query, engine)
  print(data_frame.head())
  for column in data_frame.columns: print(column)
  
  data_frame.columns = ["id", "name", "sal"]

  data_frame[["id", "name"]]

  data_frame.rename(columns = { "id": "empId", "name": "empName" }, inplace = True)
  
  data_frame.rename(columns = lambda column: column.split(".")[-1], inplace=True)

  for index, row in data_frame.iterrows(): print (row["id"], row["name"])
  

  data_frame.to_sql(con = engine, schema = "public", name = "tableName", if_exists = "append", index = False, index_label = None, chunksize = None, dtype = None, method = "multi")

  for k in conf["bitbucket.org"]:
    print(key)

  conf.items("Section")
  for k, v in conf["Section"].items():
    print(k, v)

lambda_handler(event = None, context = None)
