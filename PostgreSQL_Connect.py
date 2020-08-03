import json
import boto3

service     = "rds-data"
region_name = "us-east-1"

database    = "office_db"
schema      = "office_schema"
secretArn   = "arn:aws:secretsmanager:us-east-1:123456789012:secret:office_secret-9B15Hi"
resourceArn = "arn:aws:rds:us-east-1:123456789012:cluster:office-cluster"

def lambda_handler(event, context):

  client = boto3.client(service, region_name = region_name)

  response = client.execute_statement(
    secretArn   = secretArn,
    database    = database,
    resourceArn = resourceArn,
    sql         = sql)

  print(json.dumps(response, indent = 2))
  
  return {
    "statusCode": 200,
    "body:" json.dumps("Hello from Lambda!")
  }
