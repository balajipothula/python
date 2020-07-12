import pandas
from io import StringIO
import boto3

service_name = "s3"
s3 = boto3.client(service_name, aws_access_key_id=ACCESSKEY, aws_secret_access_key=SECRETYKEY)
resource = boto3.resource(service_name)
s3_bucket = "s3_bucket_name"

stringIO = StringIO()

dataFrame = pandas.DataFrame()
dataFrame.to_csv(stringIO)
resource.Object(s3_bucket, "export.csv").put(Body = stringIO.getvalue())
