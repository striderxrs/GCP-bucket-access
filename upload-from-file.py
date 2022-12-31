import os
from google.oauth2.credentials import Credentials

def upload_files_from_file(creds, bucket_name, file_paths_file):
    """Upload all the files specified in a file to a storage bucket in Google Cloud.

    Args:
        creds (google.oauth2.credentials.Credentials): The credentials to use to authenticate the request.
        bucket_name (str): The name of the bucket to which the files will be uploaded.
        file_paths_file (str): The path to the file containing the file paths to be uploaded.
    """
    # Read the file paths from the file.
    with open(file_paths_file, 'r') as f:
        file_paths = f.readlines()

    # Upload each file.
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        upload_file(creds, bucket_name, file_path, file_name)

# Replace the values of `YOUR_CLIENT_SECRET_FILE`, `YOUR_BUCKET_NAME`, and `YOUR_FILE_PATHS_FILE` with your own values.
creds = Credentials.from_authorized_user_info(info=None, filename='YOUR_CLIENT_SECRET_FILE')
bucket_name = 'YOUR_BUCKET_NAME'
file_paths_file = 'YOUR_FILE_PATHS_FILE'

upload_files_from_file(creds, bucket_name, file_paths_file)
