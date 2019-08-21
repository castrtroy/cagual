import urllib.request
import json
import os
import sys

getIP = sys.argv[1]
url = "https://ipinfo.io/" + getIP + "/json"

try:
    getInfo = urllib.request.urlopen(url)

except:
    print("\n[!] - IP not found! - [!]\n")

infoList = json.load(getInfo)


def whoisIPinfo(ip):
    try:

        myComand = "whois " + getIP
        whoisInfo = os.popen(myComand).read()
        return whoisInfo

    except:

        return "\n [!] -- Error -- [!] \n"

if infoList["country"] != "RU" :
    print( getIP )
