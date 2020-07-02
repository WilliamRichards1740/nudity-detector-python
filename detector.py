import requests
import json
import os
import time
from colorama import init
init()
from colorama import Fore, Back , Style 
directory = raw_input("Directory (End with '/' no backslashes allowed) :")
files = os.listdir(directory)
while files:
    try:
        time.sleep(5) # I know its unconventional, but I didn't see another way arround this 
        files2 = files.pop(1)
        print (files2)

        r = requests.post(
        "https://api.deepai.org/api/nsfw-detector",
        files={
        'image': open(directory + files2, 'rb'),
        },
        headers={'api-key': 'YOUR KEY HERE'}  #get api key at https://deepai.org/ its free! 
        )

        json = r.json()
        output = (json["output"])
        nsfw = (output["nsfw_score"])
        print("JSON OUTPUT:")
        print(json)
   
        if nsfw < 0.5:
            print(Fore.GREEN +"Safe For Work" + Fore.RESET)
         
        elif nsfw > 0.5:
            print(Fore.RED +"Not Safe For Work" + Fore.RESET)
            os.remove(directory + files2)
    except:
        pass

