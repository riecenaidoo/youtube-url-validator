# Research 

This document serves to archive the steps taken, and thought processes behind the implementation of this solution. 

## The Problem

As part of a larger project, there was a need for a way to programmatically validate large amounts YouTube URLs and determine if they still were usable links (*i.e. not listed as private, or region locked*)

### Pilot Test Code

First just sent a request to two sample links, one we know to be valid, and one we know to be invalid (*by checking manually*). 
Expectation was that the valid link would return a Response [200] OK, and the invalid Response [400+] ERROR.
Here, it was discovered that YouTube will return Response [200] for both types of links, invalid and valid. 
However, the invalid link had a different page and unplayable video. 
The second solution was to try to send a header in the Requests to disallow redirecting, under the assumption that YouTube is redirecting the URL to a default 'Video Unavailable' webpage.
However, this was not the case. 
Finally, we decide to deserialize the Response and look at what is being returned.
The response is a html page, and within the html page there was a noticeable difference between the two types of responses:
Both had a player embedded in their page, but in the invalid link, the player was disabled and set to display an error message.
Using simple requests, we can search for that pattern in the response to see if the video is playable or not i.e. if the webpage for that URL has a playable miniplayer with the playability status set to `OK`.

The advantage of this solution is that it is simplistic.

The disadvantages of this solution are major;

To validate a large amount of URLs, we would need to send a large number of requests and received a large number of responses and search through them. With a decent connection, and computer, this wouldn't take too long, but it is a very poor use of resources.
The second major disadvantage is that this is a `hack` solution, and not a permanent solution. 
    - Should the format of these webpages every change slightly, the pattern matching would break and so would this important validation service.
    - With only two sample videos links used, we can't be sure that every single valid, and invalid link would follow these formats. For instance, are the responses the same for the links of webpages in different languages or regions?

So, while this solution could work, for a limited use case, it is unlikely it could be scaled or maintained.



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

