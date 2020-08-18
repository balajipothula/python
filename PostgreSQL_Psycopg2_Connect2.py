import sys
import json
import boto3
import base64
import logging
import psycopg2
import rds_config

from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

service     = "rds-data"
region_name = "us-east-1"

database    = "emp_db"
schema      = "emp_schema"
secretArn   = ""
resourceArn = ""

host        = ""
port        = ""
user        = None
password    = None
dbname      = "emp_db"

secret      = Nones

def lambda_handler(event, context):

  session = boto3.session.Session()
  client  = session.client(service_name = "secretsmanager", region_name = region_name)
  
  try:
    secret_value = client.get_secret_value(SecretId = secretArn)
  except ClientError as clientError:
    logger.error(clientError)
    raise clientError
  else:
    if "SecretString" in secret_value:
      secret = json.loads(secret_value["SecretBinary"])
    else:
      secret = json.loads(base64.b64decode(secret_value["SecretBinary"]))
  
  try:
    if secret is not None:
      user       = secret["username"]
      password   = secret["password"]
      connection = psycopg2.connect(host = host, port = port, user = user, password = password, dbname = dbname)
      if connection is not Nono:
        print("Database connection established...")
        cursor = connection.cursor()
        sql    = "SELECT * FROM information_schema.tables"
        cursor.execute(sql)
        for record in cursor:
          print(record)
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  finally:
    if connection is not None:
      connection.close()
      print("Database connection closed...")

lambda_handler(None, None)
