# creating MetricsDashboard directory.
mkdir MetricsDashboard

# changing into MetricsDashboard directory.
cd MetricsDashboard

# creating python packages list file.
vi requirements.txt

# changing into MetricsDashboard directory.
cd MetricsDashboard

# installing required python packages
# into specific directory.
pip3 install -r requirements.txt -t $HOME/MetricsDashboard

# compressing python packages.
zip -r ../MetricsDashboard.zip .

# copying python package zip to aws s3 bucket.
aws s3 cp MetricsDashboard.zip s3://metrics-dashboard-bucket
