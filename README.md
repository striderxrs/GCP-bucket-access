<h1> Google Cloud Storage Bucket Access and File Upload </h1>

This project contains Python code for accessing a specific storage bucket in Google Cloud and uploading files to it.

Prerequisites:
------------------------
Before you can use the code in this project, you will need to have the following:

You will need to have a Google Cloud account and have set up the necessary authentication credentials.
You will need to have the following libraries installed:

google-auth
google-auth-oauthlib
google-auth-httplib2
google-api-python-client

The necessary authentication credentials to access the storage bucket (either a client secret JSON file or an access key)


Installation:
------------------------
To use the code in this project, you will need to install the following libraries:

pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client


Usage:
------------------------
Accessing a Storage Bucket

The script provides the following functions:

upload_file(creds, bucket_name, file_path, file_name): This function can be used to upload a single file to a specific storage bucket. It takes four arguments:

creds: The credentials to use to authenticate the request.
bucket_name: The name of the bucket to which the file will be uploaded.
file_path: The path to the file to be uploaded.
file_name: The name to give the file in the bucket.
upload_files_in_directory(creds, bucket_name, directory_path, interval): This function can be used to continuously check a specific directory for new files and upload them to a storage bucket at a specified interval. It takes four arguments:

creds: The credentials to use to authenticate the request.
bucket_name: The name of the bucket to which the files will be uploaded.
directory_path: The path to the directory containing the files to be uploaded.
interval: The interval, in seconds, at which to check the directory for new files and upload them.
upload_files_from_file(creds, bucket_name, file_paths_file): This function can be used to upload all the files specified in a file to a storage bucket. It takes three arguments:

creds: The credentials to use to authenticate the request.
bucket_name: The name of the bucket to which the files will be uploaded.
file_paths_file: The path to the file containing the file paths to be uploaded. The file should have one file path per line.

This code will authenticate your Python script and use the google-api-python-client library to access the storage bucket with the name specified in the bucket_name variable. If the bucket is found, it will print a message indicating that the bucket was found. If the bucket is not found or if there is an error accessing the bucket, it will print an error message.

You can also use an access key to authenticate your Python script instead of using a client secret JSON file. To do this, you can use the google-auth library's GoogleCredentials.from_access_key method to create a Credentials object using the access key. 


