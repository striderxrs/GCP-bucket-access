""" You can also use an access key to authenticate your Python script instead of using a client secret JSON file.
To do this, you will need to use the google-auth library's GoogleCredentials.from_access_key method to create a
Credentials object using the access key. Here is an example of how you can do this: """

# First, you will need to install the necessary libraries:
# !pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

from google.oauth2.credentials import Credentials

# Replace the values of `YOUR_ACCESS_KEY_ID` and `YOUR_SECRET_ACCESS_KEY` with your own access key ID and secret access key.
access_key_id = 'YOUR_ACCESS_KEY_ID'
secret_access_key = 'YOUR_SECRET_ACCESS_KEY'

# Use the `GoogleCredentials.from_access_key` method to create a `Credentials` object using the access key.
creds = Credentials.from_access_key(access_key_id, secret_access_key)

# Now that you have the necessary credentials, you can use the `google-api-python-client` library to access your storage bucket.

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Replace the value of `YOUR_BUCKET_NAME` with the name of your bucket.
bucket_name = 'YOUR_BUCKET_NAME'

# Create a service client.
service = build('storage', 'v1', credentials=creds)

# Use the service client to access the bucket.
try:
    bucket = service.buckets().get(bucket=bucket_name).execute()
    print(f'Bucket {bucket_name} was found.')
except HttpError as error:
    print(f'An error occurred while trying to access the bucket: {error}')

