import sys
import json
import boto3
import logging
import psycopg2
import rds_config

def lambda_handler(event, context):

  logger = logging.getLogger()
  logger.setLevel(logging.INFO)
  
  try:
    connection = rds_config.initiateConnection()
    logger.info("Connection to RDS Aurora PostgreSQL instance succeeded...")
    
    queries = (
      """
      SELECT * FROM information_schema.tables;
      """,)
      
    try:
      cur = connection.cursor()
      
      for query in queries:
        errflag = False
        cur.execute(query)
      
      rows = []
      for row in cur:
        rows.append(row)
      
      print(rows)
      
      cur.close()
      connection.commit()
      
    except (Exceptionm psycopg2.DatabaseError) as e:
      errflag = True
      logger.error(e)
    finally:
      if not errflag:
        logger.info("Artifacts creation successfull...")
      if connection is not None:
        connection.close()
    
    logger.info("DB Connection Closed")

  except (Exception, psycopg2.DatabaseError) as e:
    logger.error("ERROR: Unexpected error: Could not connect to Aurora PostgreSQL instance")
    logger.error(e)
    sys.exit()

lambda_handler(None, None)
