import os
import math
import dask.dataframe as dd
import numpy as np
import pandas as pd

from dask.distributed import Client

# Setup for Dask needs to be available before running this test
print("Dask setup not configured, can't execute test")
exit(0)

os.environ['LOCALSTACK_S3_ENDPOINT_URL'] = 'http://localhost:5000'

client = Client('tcp://scheduler:8786')
# Lets toggle localstack by changing where boto3 is pointing to
if os.environ.get('LOCALSTACK_S3_ENDPOINT_URL'):
    taxi_data = dd.read_csv('s3://nyc-tlc/trip data/yellow_tripdata_2018-04.csv',
                            storage_options={
                                'anon': True,
                                'use_ssl': False,
                                'key': 'foo',
                                'secret': 'bar',
                                "client_kwargs": {
                                    "endpoint_url": os.environ.get('LOCALSTACK_S3_ENDPOINT_URL'),
                                    "region_name": "us-east-1"
                                }
                            }
                            )
else:
    # This assumes your using named profiles in aws cli with a default profile accessing your s3 bucket or EC2
    # instance or ECS task role
    taxi_data = dd.read_csv(
        's3://nyc-tlc/trip data/yellow_tripdata_2018-04.csv')

taxi_data.head()
