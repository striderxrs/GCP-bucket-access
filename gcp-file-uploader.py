

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

def upload_file(creds, bucket_name, file_path, file_name):
    """Upload a file to a specific storage bucket in Google Cloud.

    Args:
        creds (google.oauth2.credentials.Credentials): The credentials to use to authenticate the request.
        bucket_name (str): The name of the bucket to which the file will be uploaded.
        file_path (str): The path to the file to be uploaded.
        file_name (str): The name to give the file in the bucket.
    """
    # Create a service client.
    service = build('storage', 'v1', credentials=creds)

    # Use the service client to create a MediaFileUpload object.
    media = MediaFileUpload(file_path, mimetype='application/octet-stream')

    # Use the service client to upload the file to the bucket.
    try:
        response = service.objects().insert(bucket=bucket_name, name=file_name, media_body=media).execute()
        print(f'File {file_name} was uploaded to bucket {bucket_name}.')
    except HttpError as error:
        print(f'An error occurred while trying to upload the file: {error}')
