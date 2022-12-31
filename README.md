Google Cloud Storage Bucket Access and File Upload

This project contains Python code for accessing a specific storage bucket in Google Cloud and uploading files to it.

Prerequisites:
------------------------
Before you can use the code in this project, you will need to have the following:

A Google Cloud account
A storage bucket in Google Cloud
The necessary authentication credentials to access the storage bucket (either a client secret JSON file or an access key)


Installation:
------------------------
To use the code in this project, you will need to install the following libraries:

pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client


Usage:
------------------------
Accessing a Storage Bucket

This code will authenticate your Python script and use the google-api-python-client library to access the storage bucket with the name specified in the bucket_name variable. If the bucket is found, it will print a message indicating that the bucket was found. If the bucket is not found or if there is an error accessing the bucket, it will print an error message.

You can also use an access key to authenticate your Python script instead of using a client secret JSON file. To do this, you can use the google-auth library's GoogleCredentials.from_access_key method to create a Credentials object using the access key. 
