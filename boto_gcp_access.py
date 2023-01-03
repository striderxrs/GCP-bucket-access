import boto
from boto.gs.connection import GSConnection

# Set the access key ID and secret access key.
access_key_id = 'your_access_key_id'
secret_access_key = 'your_secret_access_key'

# Connect to the Google Cloud Storage service using the access key ID and secret access key.
gs_connection = GSConnection(access_key_id, secret_access_key)
storage_client = boto.connect_gs(gs_connection=gs_connection)

# List the contents of the storage bucket.
bucket = storage_client.get_bucket('my-bucket')
for key in bucket.list():
    print(key.name)
