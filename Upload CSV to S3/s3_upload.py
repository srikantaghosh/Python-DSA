import os
import boto3


#instantiate client
client = boto3.client('s3')

# set variables
bucket = 'vscodeupload3012'
cur_path = os.getcwd()

file = 'crypto_api.csv'


filename = '/Applications/Ramos/Coding Repo/ProjectLord/crypto.csv'


data = open(filename, 'rb')

client.upload_file(filename, bucket, file)