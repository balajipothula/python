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
  
  parameters = [
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

  response = client.execute_statement(
    continueAfterTimeout  = False,
    database              = database,
    includeResultMetadata = True,
    parameters            = parameters,
    resourceArn           = resourceArn,
    resultSetOptions      = {"decimalReturnType": "STRING"},
    schema                = schema,
    secretArn             = secretArn,
    sql                   = sql)

  print(json.dumps(response, indent = 2))

lambda_handler(None, None)
