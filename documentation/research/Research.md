# Research 

This document serves to archive the steps taken, and thought processes behind the implementation of this solution. 

## The Problem

As part of a larger project, there was a need for a way to programmatically validate large amounts YouTube URLs and determine if they still were usable links (*i.e. not listed as private, or region locked*)

### Pilot Test Code

    import requests
    
    urls = {
        (True, 200, "https://www.youtube.com/watch?v=g_FTlm3tdoU"),
        (False, 200, "https://www.youtube.com/watch?v=g_FTlm3sdq12tdoU"),
    }
    
    response = requests.get("https://www.youtube.com/watch?v=g_FTlm3tdoU")
    
    lines = response.text.split("\n")
    print(f"Receive Response of {len(lines)} lines.")
    
    with open("sample/response.txt", 'w') as f:
        f.write(response.text)
    
    print("DONE.")

### HTTP Request

When sending the request, both the valid and invalid video links return a Response OK [200].

In `response.txt` :

Valid Link (Can be Played):

    "playabilityStatus":{
        "status":"OK",
        "playableInEmbed":true,
        "miniplayer":{
            "miniplayerRenderer":{
                "playbackMode":"PLAYBACK_MODE_ALLOW"
                }
            }


Invalid Link (Can't be Played):

    "playabilityStatus":{
        "status":"ERROR",
        "reason":"Video unavailable",
        "errorScreen":{
            "playerErrorMessageRenderer":{
                "reason":{
                    "simpleText":"Video unavailable"
                    }


## API

Guides:
https://developers.google.com/youtube/v3/docs/videos/list

Request (A Valid Link):

    part = player,
    
    id = ["g_FTlm3tdoU"]

Response [200]:

    {
      "kind": "youtube#videoListResponse",
      "etag": "RlDtdRP6Xd1VqBxCwYIl5Bov5OE",
      "items": [
        {
          "kind": "youtube#video",
          "etag": "b3lVeWd0gdg04QXmhq1npQl4bEg",
          "id": "g_FTlm3tdoU"
        }
      ],
      "pageInfo": {
        "totalResults": 1,
        "resultsPerPage": 1
      }
    }


Request (An Invalid Link):

    part = player,
    
    id = ["g_FTlm3sdq12tdoU"]

Response [200]:

    {
      "kind": "youtube#videoListResponse",
      "etag": "YIUPVpqNjppyCWOZfL-19bLb7uk",
      "items": [],
      "pageInfo": {
        "totalResults": 0,
        "resultsPerPage": 0
      }
    }


Request (Valid and Invalid Links):

    part = player,
    
    id = ["g_FTlm3sdq12tdoU", "g_FTlm3tdoU"]

Response [200] : 

    {
      "kind": "youtube#videoListResponse",
      "etag": "C3GDSygg6sGslJhiuaFSsjlryGI",
      "items": [
        {
          "kind": "youtube#video",
          "etag": "N9qxkiuw0jSL2KzSX9HqDdhhNwk",
          "id": "g_FTlm3tdoU",
          "player": {
            "embedHtml": "\u003ciframe width=\"480\" height=\"270\" src=\"//www.youtube.com/embed/g_FTlm3tdoU\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" allowfullscreen\u003e\u003c/iframe\u003e"
          }
        }
      ],
      "pageInfo": {
        "totalResults": 1,
        "resultsPerPage": 1
      }
    }

