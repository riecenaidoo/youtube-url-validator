# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    # Disabling this currently seems to work fine?
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"

    # Get credentials  client
    # client_secrets_file = "config/client_secret.json"
    # flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    #     client_secrets_file, scopes)
    # credentials = flow.run_local_server(port=0)
    # youtube = googleapiclient.discovery.build(
    #     api_service_name, api_version, credentials=credentials)

    # Use Developer Key
    with open("config/api_key.txt", "r") as f:
        key = f.readline()

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=key)

    links_to_validate = {
        "g_FTlm3sdq12tdoU",
        "g_FTlm3tdoU"
    }

    request = youtube.videos().list(
        part="player",
        id="g_FTlm3sdq12tdoU,g_FTlm3tdoU"
    )

    response = request.execute()
    # print(response)

    valid_links = set()
    for item in response.get("items"):
        valid_links.add(item.get("id"))

    invalid_links = set.difference(links_to_validate, valid_links)
    print(f"These are invalid links : {invalid_links}")


if __name__ == "__main__":
    main()
