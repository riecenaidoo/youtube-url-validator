# youtube-url-validator

## Test Code

    import requests
    
    urls = {
        (True, 200, "https://www.youtube.com/watch?v=g_FTlm3tdoU"),
        (False, 200, "https://www.youtube.com/watch?v=g_FTlm3sdq12tdoU"),
    }
    
    response = requests.get("https://www.youtube.com/watch?v=g_FTlm3tdoU")
    
    lines = response.text.split("\n")
    print(f"Receive Response of {len(lines)} lines.")
    
    with open("sample/response.html", 'w') as f:
        f.write(response.text)
    
    print("DONE.")

## HTTP Request

In `response.text` :

Can be Played:

    "playabilityStatus":{
        "status":"OK",
        "playableInEmbed":true,
        "miniplayer":{
            "miniplayerRenderer":{
                "playbackMode":"PLAYBACK_MODE_ALLOW"
                }
            }


Can't be Played:

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

Request:

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
