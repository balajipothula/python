import sys
import logging
import pymysql

# rds settings
rds_host  = "myDatabase.ghfghghgf.us-east-1.rds.amazonaws.com"
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

# logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
  connect = pymysql.connect(rds_host, user=user, passwd=passwd, db=db, connect_timeout=5)
except:
  logger.error("Could not connect to MySql instance.")
  sys.exit()

logger.info("Connection to RDS MySQL instance succeeded")

# array to store values to be returned
records = []

# executes upon API event
def handler(event, context):
  with connect.cursor() as cursor:
    cursor.execute("SELECT no, name, sal FROM emp")
    connect.commit()
    for emp in cursor:
      record = { "no": emp[1], "name": emp[2], "sal": emp[3] }
      records.append(record)
    return records
