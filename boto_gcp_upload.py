"""
Set up a service account and grant it the necessary permissions to access the storage bucket.

Install the Boto library and set the access key ID and secret access key.

Connect to the Google Cloud Storage service using the access key ID and secret access key.

Retrieve the storage bucket and create a new Key object for the file you want to upload.

Use the Key object's set_contents_from_filename method to upload the file to the storage bucket.
"""
import boto
from boto.gs.connection import GSConnection

# Set the access key ID and secret access key.
access_key_id = 'your_access_key_id'
secret_access_key = 'your_secret_access_key'

# Connect to the Google Cloud Storage service using the access key ID and secret access key.
gs_connection = GSConnection(access_key_id, secret_access_key)
storage_client = boto.connect_gs(gs_connection=gs_connection)

# Retrieve the storage bucket and create a new Key object for the file.
bucket = storage_client.get_bucket('my-bucket')
key = bucket.new_key('my-file.txt')

# Upload the file to the storage bucket.
key.set_contents_from_filename('/path/to/my-file.txt')
