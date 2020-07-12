from elasticsearch import exceptions
from elasticsearch import Elasticsearch
from elasticsearch import RequestsHttpConnection

from elasticsearch_dsl import Search

from requests_aws4auth import AWS4Auth

import boto3
import json

# AWS Region Name.
region_name = "us-east-1"

# AWS Service Name.
service = "es"

# AWS Elasticsearch service URL / Host name.
host = "Elasticsearch_Service_URL"

# AWS Elasticsearch service port / Host port.
port = 443

def lambda_handler(event, context):

  # Create CloudWatch Client.
  client = boto3.client(service, region_name =  region_name)
  
  # Get Elasticsearch Domain Names.
  response = client.list_domain_names()

  # Get AWS Credentials (Access and Secret Keys)
  credentials = boto3.Session().get_credentials()

  # Get AWS HTTP Authorization.
  http_auth = AWS4Auth(credentials.access_key,
                       credentials.secret_key,
                       region,
                       service,
                       session_token = credentials.token)

  # Get Elastcisearch Client.
  es = Elastcisearch(hosts = [ { "host": host, "port": port } ],
                         http_auth = http_auth,
                         use_ssl = True,
                         verify_certs = True,
                         connection_class = RequestsHttpConnection)
  
  print(es.info())
  
  try:
    indices  = es.indices.get("kibana_sample_data_*")
    for index in indices:
      print(index)
  except exception.ConnectionError as error:
    print(error)

  index     = "kibana_sample_data_logs"
  doc_type  = "_doc"
  search    = Search(using = es, index = index, doc_type = doc_type)
  from_date = "2020-07-07T18:30:00.000Z"
  to_date   = "2020-07-07T19:30:00.000Z"
  filter    = search.filter( "range", timestamp = { "gte": from_date, "lte": to_date } )
  order     = "asc"
  sort      = filter.sort( { "@timestamp": { "order": order } } )
  source    = sort.source([])
  ids       = [ hit.meta.id for hit in source.scan() ]
  
  for id in ids:
    response = es.get(index = index, id = id)
    print(json.dumps(response, indent = 2))
