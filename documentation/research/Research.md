# Research 

This document serves to archive the steps taken, 
and thought processes behind the implementation of this solution. 

## The Problem

As part of a larger project, 
there was a need for a way to programmatically validate large amounts of YouTube URLs and,
determine if they still were usable links (*i.e. not listed as private, or region locked*)

## Solution 1: HTTP Requests

The first attempted solution was based on HTTP Requests.
The thought process was that an invalid like would return an error response (400+).

### Iteration 1

First, we send a request to fetch two sample links, one we know to be valid, and one we know to be invalid (*by checking manually*). 
The expectation was that the valid link would return a Response `200+` (OK), and the invalid Response `400+` (ERROR).

Code:

    import requests
    
    valid_link_response = requests.get("https://www.youtube.com/watch?v=g_FTlm3tdoU")
    invalid_link_response = requests.get("https://www.youtube.com/watch?v=g_FTlm3sdq12tdoU")
    
    print(f"Valid Link Response Code: {valid_link_response.status_code}")
    print(f"Invalid Link Response Code: {invalid_link_response.status_code}")

Output:

    Valid Link Response Code: 200
    Invalid Link Response Code: 200
    
    Process finished with exit code 0

*Here, it was discovered that YouTube will return Response `200` (OK) for both invalid and valid links.*

### Iteration 2

However, there was a noticeable difference between the two links, when viewed manually. 
The invalid link had a slightly different page layout, with an unplayable embedded video player,
with the static message, 'Video Unavailable' displayed.

The second solution was to try to send a header in the Requests to disallow redirecting, 
under the assumption that YouTube is redirecting the invalid URL to a default 'Video Unavailable' webpage.

Code:

    import requests
    
    valid_link_response = requests.get("https://www.youtube.com/watch?v=g_FTlm3tdoU", allow_redirects=False)
    invalid_link_response = requests.get("https://www.youtube.com/watch?v=g_FTlm3sdq12tdoU", allow_redirects=False)
    
    print(f"Valid Link Response Code: {valid_link_response.status_code}")
    print(f"Invalid Link Response Code: {invalid_link_response.status_code}")

Output:

    Valid Link Response Code: 200
    Invalid Link Response Code: 200
    
    Process finished with exit code 0

*However, this was not the case, the URL was not being redirected, but the invalid video link was handled internally on the server end.* 

### Iteration 3

Finally, we decide to deserialize the Response and look at what is being returned.

Code:

    import requests
    
    valid_link_response = requests.get("https://www.youtube.com/watch?v=g_FTlm3tdoU", allow_redirects=False)
    invalid_link_response = requests.get("https://www.youtube.com/watch?v=g_FTlm3sdq12tdoU", allow_redirects=False)
    
    with open("valid_response.txt", "w") as f:
        f.write(valid_link_response.text)
    
    with open("invalid_response.txt", "w") as f:
        f.write(invalid_link_response.text)


The responses are HTML pages, which we could view in an easier-to-read format in a code editor. 
Within the html page there was a noticeable difference between the two types of responses:

In `valid_response.html` :

    "playabilityStatus":{
        "status":"OK",
        "playableInEmbed":true,
        "miniplayer":{
            "miniplayerRenderer":{
                "playbackMode":"PLAYBACK_MODE_ALLOW"
                }
            }

In `invalid_response.html` :

    "playabilityStatus":{
        "status":"ERROR",
        "reason":"Video unavailable",
        "errorScreen":{
            "playerErrorMessageRenderer":{
                "reason":{
                    "simpleText":"Video unavailable"
                    }


Both had a player embedded in their page, but in the invalid link, the player was disabled and set to display an error message.

### Summary

#### Potential Solution
Using simple HTTP requests, we can search the HTML page response for the aforementioned pattern to see if the video is playable or not 
i.e. if the webpage for that URL has a playable mini-player with the playability status set to `OK`.

#### Advantages
The advantage of this solution is that it is simplistic.

#### Disadvantages
The disadvantages of this solution are major;

1. To validate a large number of URLs, we would need to send and receive HTTP requests/responses and search through each of them individually. 
With a decent connection, and computer, this wouldn't take too long, but it is a very poor use of resources.
2. The second major disadvantage is that this is a **hack** solution and not a permanent solution. 
    - Should the format of these webpages ever change slightly, the pattern matching would break, which would break this validation script.
    - With only two sample video links used, we can't be sure that every single valid, and invalid link,
   would follow these formats. For instance, are the responses the same for the links to web pages in different languages or regions?

#### Conclusion
While this solution could work, for a limited use case, it is unlikely it could be scaled or maintained. Another solution is needed.

## Solution 2: YouTube Data API

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

### Summary

The YouTube Data API provides a way to check large amounts of links, and will not be protected from being outdated*
