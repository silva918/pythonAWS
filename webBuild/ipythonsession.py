# ipython setup file
import boto3
session = boto3.Session(profile_name='calmCluster')
s3 = session.resource('s3')
