#   README
An example of a Python script using the YouTube Data API to validate YouTube video links
and query which videos are no longer available for viewing.
Intended to be used for a cross-platform playlist management system.


## Requirements

You'll need the following :

- `Pip` (*To install dependencies*)
- `Google Account` (*To set up your project credentials*)
- `Python` (*To run the script*)


## Setup

To run the script, you'll need to follow four steps:
1. Install Dependencies
2. Setup Project Credentials
3. Configure the `main.py` Script
4. Run the Script

### Install Dependencies:

*It is recommended you set up a virtual environment to work in.*

Install `google-api-python-client`, `google-auth-oauthlib`, and `google-auth-httplib2` via pip package management tool.

    pip install google-api-python-client google-auth-oauthlib google-auth-httplib2

Install Kivy if running the GUI

    pip instal kivy

### Setup Project Credentials:

*To follow the next steps, and demo this project,
you'll need to use your `Google Account` to sign in to the
[Google API Console](https://console.cloud.google.com/).
From there you'll need to [Create or select an existing project](https://developers.google.com/youtube/v3/quickstart/python#step_1_set_up_your_project_and_credentials) to set up your project credentials.*

### Configure the `main.py` Script

For the next step, you'll need either your **API Key**, or your **Client Secret** file. 
Whichever method you are using, make sure they are kept secret, and **not publicly visible**.
Anyone with access to them can make calls to the YouTube Data API using your credentials.

#### Using API Key

The simplest, and fastest, way to test this script is with your API key.
 1. Copy your key
 2. Save it in a file, e.g. `config/dev_key.txt`
     - *If you choose to save it elsewhere, copy the path and pass it as the argument in the function call `youtube.dev_auth()`*

#### Using 0Auth

 Alternatively, you can use 0Auth.
1. Download your Client Secret file.
2. Save it in an accessible location, e.g. `config/client_secret.json`
3. Replace the `youtube.dev_auth()` call in the script, with `youtube.client_auth()`
4. Pass the path to your Client Secret file as the argument of the function call.

### Run the Script

- Add YouTube video IDs you'd like to validate to the set `ids_to_validate` in `main.py`
- Execute the script