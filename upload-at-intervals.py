"""To upload files from a specific folder at certain time intervals, you can use the time and os libraries in Python
to check the directory for new files and schedule the uploads using the upload_file function.
"""

import os
import time

from google.oauth2.credentials import Credentials


def upload_files_in_directory(creds, bucket_name, directory_path, interval):
    """Upload all the files in a specific directory to a storage bucket in Google Cloud at a specified interval.

    Args:
        creds (google.oauth2.credentials.Credentials): The credentials to use to authenticate the request.
        bucket_name (str): The name of the bucket to which the files will be uploaded.
        directory_path (str): The path to the directory containing the files to be uploaded.
        interval (int): The interval, in seconds, at which to check the directory for new files and upload them.
    """
    while True:
        # Get a list of all the files in the directory.
        files = os.listdir(directory_path)

        # Upload each file in the directory.
        for file in files:
            file_path = os.path.join(directory_path, file)
            upload_file(creds, bucket_name, file_path, file)

        # Wait for the specified interval before checking the directory again.
        time.sleep(interval)


# Replace the values of `YOUR_CLIENT_SECRET_FILE`, `YOUR_BUCKET_NAME`, `YOUR_DIRECTORY_PATH`,
# and `YOUR_UPLOAD_INTERVAL` with your own values.
creds = Credentials.from_authorized_user_info(info=None, filename='YOUR_CLIENT_SECRET_FILE')
bucket_name = 'YOUR_BUCKET_NAME'
directory_path = 'YOUR_DIRECTORY_PATH'
upload_interval = YOUR_UPLOAD_INTERVAL  # in seconds

upload_files_in_directory(creds, bucket_name, directory_path, upload_interval)
