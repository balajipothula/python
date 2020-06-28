import boto3

from datetime import datetime
from datetime import timedata

# AWS Region Name.
region_name  = "us-east-1"

# Getting AWS CloudWatch Client.
client       = boto3.client("cloudwatch", region_name = region_name)

# AWS NameSpace / AWS Service Name.
NameSpace    = "AWS/S3"

# AWS S3 Bucket Metric Name. 
MetricName   = "BucketSizeBytes"

# AWS S3 Dimensions (Bucket Name, Storage Type, ...)
Dimensions   = [
  { "Name": "BucketName",  "Value": "S3_Bucket_Name"  },
  { "Name": "StorageType", "Value": "StandardStorage" }
]

# Start time frame.
StartTime    = datetime.utcnow() - timedelta(days = 6)

# End time frame.
EndTime      = datetime.utcnow()

# Time period, 1 Day - 24 Hours - 86400 Seconds, 1 Hour - 3600 Seconds.
Period       = 86400

# Statistic type.
Statistics   = ["Average"]

# Unit type.
Unit         = "Bytes"

# Getting corresponding Metric response dictionary.
response     = client.get_metric_statistics(
  NameSpace  = NameSpace
  MetricName = MetricName
  Dimensions = Dimensions
  StartTime  = StartTime
  EndTime    = EndTime
  Period     = Period
  Statistics = Statistics
  Unit       = Unit
)

Datapoints   = response["Datapoints"]

if 0 == len(Datapoints):
  print("No Datapoints")
else:
  for Datapoint in Datapoints:
    print("MetricName: " + response["Label"])
    print("Timestamp : " + str(Datapoint["Timestamp"]))
    print("Average   : " + str(Datapoint["Average"]))
    print()
