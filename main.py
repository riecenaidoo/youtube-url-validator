import requests

urls = {
    (True, 200, "https://www.youtube.com/watch?v=g_FTlm3tdoU"),
    (False, 200, "https://www.youtube.com/watch?v=g_FTlm3sdq12tdoU"),
}

response = requests.get("https://www.youtube.com/watch?v=g_FTlm3tdoU")

lines = response.text.split("\n")
print(f"Receive Response of {len(lines)} lines.")

with open("response.html", 'w') as f:
    f.write(response.text)

print("DONE.")

"""
In response.text :

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
                
"""
