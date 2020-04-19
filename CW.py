import boto3

client = boto3.client('logs')

logGroupName = "myloggroup"

queryString  = """
FILTER  @message IN "ERROR           |
PARSE   @message "* [*] *" as @error |
DISPLAY @error                       |
LIMIT   1
""".strip()

print(queryString)

response = client.start_query(logGroupName='string', queryString='string')
