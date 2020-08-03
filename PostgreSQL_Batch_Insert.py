import json
import boto3

service     = "rds-data"
region_name = "us-east-1"

database    = "office_db"
schema      = "office_schema"
secretArn   = "arn:aws:secretsmanager:us-east-1:123456789012:secret:office_secret-9B15Hi"
resourceArn = "arn:aws:rds:us-east-1:123456789012:cluster:office-pg-cluster"

def lambda_handler(event, context):

  client = boto3.client(service, region_name = region_name)
  
  parameterSets = []
  
  parameterSet = [
    { "name": "no",   "value": {"stringValue": "101"} },
    { "name": "name", "value": {"stringValue": "Balaji"} },
    { "name": "sal",  "value": {"stringValue": "78395.81"} } ]
  
  sql = """INSERT INTO emp_db.emp_schema.emp_tab(
             no,
             name,
             sal)
           VALUES(
             :no,
             :name,
             :sal)"""

  parameterSets.append(parameterSet)

  response = client.batch_execute_statement(
    database      = database,
    parameterSets = parameterSets,
    resourceArn   = resourceArn,
    schema        = schema,
    secretArn     = secretArn,
    sql           = sql)

  print(json.dumps(response, indent = 2))

lambda_handler(None, None)
