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
