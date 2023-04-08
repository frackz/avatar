import requests

TOKEN = "" # Token here

URL = "https://discord.com/api/v8/users/"
CDN = "https://cdn.discordapp.com/avatars/"

CHUNK_SIZE = 4096

def getUser(id):
    return requests.get(URL + id, headers = {
        "authorization": TOKEN
    })

def createFile(id, saved):
    with open(id+".png", "wb") as f:
        for chunk in saved.iter_content(CHUNK_SIZE):
            if chunk:
                f.write(chunk)

while True:
    id = input("User ID: ")
    user = getUser(id)

    if user.status_code != 200:
        print("This user does not exist - or cannot be accessed.")
    else:
        print("Avatar is found, saving...")
        avatar = f"{CDN}{id}/{avatar}.png"
        
        saved = requests.get(avatar, stream = True)
        createFile(id, saved)
