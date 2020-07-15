import json
import boto3

region_name = "us-east-1"
secretArn   = "arn:aws:secretsmanager:us-east-1:123456789012:secret:office_secret-9B15Hi"
database    = "office"
resourceArn = "arn:aws:rds:us-east-1:123456789012:cluster:office-pg-cluster"
sql         = "SELECT tablename FROM pg_catalog.pg_tables ORDER BY tablename"

client = boto3.client("rds-data", region_name = region_name)

def lambda_handler(event, context):
  response = client.execute_statement(
    secretArn   = secretArn,
    database    = database,
    resourceArn = resourceArn,
    sql         = sql
  )

  print(json.dumps(response, indent = 2))
  
  return {
    "statusCode": 200,
    "body:" json.dumps("Hello from Lambda!")
  }
