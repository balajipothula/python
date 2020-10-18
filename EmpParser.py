import json
import pandas
import Emp

import boto3
import base64
import logging

import time
import Emp

from botocore.exceptions import ClientError

from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from configparser import ConfigParser

log = logging.getLogger(name = "Parser")
log.setLevel(logging.INFO)

parser = ConfigParser()
parser.read("emp.conf")

# PostgreSQL connection details.
dialect    = parser.get("PostgreSQL", "dialect")
driver     = parser.get("PostgreSQL", "driver")
database   = parser.get("PostgreSQL", "database")
regionName = parser.get("PostgreSQL", "regionName")
secretName = parser.get("PostgreSQL", "secretName")

# Emp JSON variables path
empNamePath           = parser.get("Emp", "namePath")
empSurnamePath        = parser.get("Emp", "surnamePath")
empContactNumbersPath = parser.get("Emp", "contactNumbersPath")
empEmailPath          = parser.get("Emp", "emailPath")

# Joining child nodes with their respective parent nodes.
def crossJoin(left, right):
  return left.assign(key = 1).merge(right.assign(key = 1), on = "key", how = "outer").drop("key", 1)


# Converting JSON to Pandas DataFrame.
def jsonToDataFrame(json):
  def toDataFrame(data, previousKey = None):
    if isinstance(data, dict):
      dataFrame = pandas.DataFrame()
      for key in data:
        if previousKey is not None:
          dataFrame = crossJoin(dataFrame, toDataFrame(data[key], previousKey + '.' + key))
        else:
          dataFrame = crossJoin(dataFrame, toDataFrame(data[key], key))
    elif isinstance(data, list):
      dataFrame = pandas.DataFrame()
      for i in range(len(data)):
        dataFrame = pandas.concat([dataFrame, toDataFrame(data[i], previousKey)])
    else:
      dataFrame = pandas.DataFrame({previousKey[0:]: [data]})
    return dataFrame
  return toDataFrame(json)

# Parsing Pandas Data Frame and inserting Emp objects into List.
def getEmpList(dataFrame):
  empList = list()
  for i, row in dataFrame.iterrows():
    name           = row[empNamePath]
    surname        = row[empSurnamePath]
    contactNumbers = row[empContactNumbersPath]
    email          = row[empEmailPath]
    if ( name           and
         surname        and
         contactNumbers and
         email ):
      emp = Emp.Emp(name           = name,
                    surname        = surname,
                    contactNumbers = contactNumbers,
                    email          = email)
      print(emp)
      empList.insert(i, emp)
  return empList

# Getting credentials from AWS Secrets Manager.
def getCredentialJson(regionName, secretName):
  # Create a Secrets Manager client
  session = boto3.session.Session()
  client  = session.client(
    service_name = "secretsmanager",
    region_name  = region_name)
  try:
    secretValue = client.get_secret_value(SecretId = secretName)
  except ClientError as clientError:
    logging.basicConfig(filename="parser.log", level=logging.CRITICAL)
    exception = clientError.response["Error"]["Code"]
    if exception == "DecryptionFailureException":
      log.error("Secrets Manager can not decrypt the protected secret text using the provided KMS key.")
    elif exception == "InternalServiceErrorException":
      log.error("An error occurred on the server side.")
    elif exception == "InvalidParameterException":
      log.error("The request had invalid params:", str(clientError))
    elif exception == "InvalidRequestException":
      log.error("The request was invalid due to:", str(clientError))
    elif exception == "ResourceNotFoundException":
      log.error("The requested secret" + secretName + "was not found")
  else:
    if "SecretString" in secretValue:
      return json.loads(secretValue["SecretString"])
    else:
      return json.loads(base64.b64decode(secretValue["SecretBinary"]))
  finally:
    pass


def insertObjects(url, objectList):
  try:
    #engine = create_engine(url, echo = True, connect_args = {"connect_timeout": 60})
    engine      = create_engine("sqlite:///:memory:", case_sensitive = True, convert_unicode = False, echo = True, encoding = "utf-8")
    session = sessionmaker(bind = engine)()
    session.add_all(objectList)
    session.commit()
  except SQLAlchemyError as sqlAlchemyError:
    logging.basicConfig(filename = "parser.log", level = logging.CRITICAL)
    log.error("Unable to insert records / objects:" + str(sqlAlchemyError))
  finally:
    pass


def lambda_handler(event, context):
  with open(file = "emp.json", mode = "r") as empFile: empDict = json.load(empFile)
  dataFrame = jsonToDataFrame(empDict)
  empList = getEmpList(dataFrame)
  """
  postgresql = getCredentialJson(regionName = regionName, secretName = secretName)
  url = URL(drivername = dialect + "+" + driver,
            username   = postgresql["username"],
            password   = postgresql["password"],
            host       = postgresql["host"],
            port       = postgresql["port"],
            database   = database,
            query      = None)
  url = URL(drivername = dialect + "+" + driver,
            username   = "wnccpibb",
            password   = "X8OQZkwKPngIOi0KkA1Ab1culTz7y524",
            host       = "salt.db.elephantsql.com",
            port       = 5432,
            database   = "wnccpibb",
            query      = None)
  """
  insertObjects(url = None, objectList = empList)


lambda_handler(event = None, context = None)
