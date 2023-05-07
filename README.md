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

1. Install Dependencies:

   *It is recommended you set up a virtual environment to work in.*

   Install `google-api-python-client`, `google-auth-oauthlib`, `google-auth-httplib2` via pip package management tool.

        pip install google-api-python-client google-auth-oauthlib google-auth-httplib2

2. Setup Credentials:

   *To follow the next steps, and demo this project,
   you'll need to use your `Google Account` to sign in to the
   [Google API Console](https://console.cloud.google.com/).
   From there you'll need to [Set up or select an existing project](https://developers.google.com/youtube/v3/quickstart/python#step_1_set_up_your_project_and_credentials) to set up your project credentials.*

   The simplest, and fastest, way to test this script is with your API key.
    1. Copy your key
    2. Save it in a file, for e.g. `config/dev_key.txt`
        1. *If you choose to save it elsewhere, copy the path and pass it as the argument in the function call `youtube.dev_auth()`*
        2. *If the path is inside this repo, add it to the `.gitignore` - **your API key should be kept secret and not publicly visible.***

    Alternatively, you can use 0Auth.
   1. Download your Client Secret file.
   2. Save it in an accessible location, for e.g. `config/client_secret.json`
   3. Replace the `youtube.dev_auth()` call in the script, with `youtube.client_auth()`, pass the path to your Client Secret file as the argument.
      1. *If the path is inside this repo, add it to the `.gitignore` - **keep it secret and not publicly visible.***
