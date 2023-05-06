# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
# Disabling this currently seems to work fine?
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"


def client_auth(client_secret_path):
    # Get credentials client
    client_secrets_file = client_secret_path
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server(port=0)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    return youtube


def dev_auth(dev_key_path):
    # Use Developer Key
    with open(dev_key_path, "r") as f:
        key = f.readline()

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=key)

    return youtube
