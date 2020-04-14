import boto3

client = boto3.client('logs')

#logGroupName  =
#logGroupNames =
#startTime     =
#endTime       =
#queryString   =
#limit         =

response = client.start_query(logGroupName='string', logGroupNames=['string', ], startTime=123, endTime=123, queryString='string', limit=123)
