__author__ = 'stamse'
import csv
import json
import urllib.request
from urllib import request

x = "http://hackerleague.org/api/v1/hackathons.json?limit=2&offset=1"

#y = json.loads(x)

print (x)
#f = open('data.json')
#data = json.load(f)
#f.close()

def downloadJsonDataFromUrl(json_url):
    response = request.urlopen(json_url)
    json1 = response.read()
    json1_string = str(json1)
    lines = json1_string.split("\\n")
    destination_url = "downloadedJsonFileOfHackathons2.json"
   # destination_url_txt = "downloadedFileOf"+inputValue+"Hackathons.txt"
    jsonFileOpen = open(destination_url, "w")
    for line in lines:
        jsonFileOpen.write(line + "\n")
    jsonFileOpen.close()

downloadJsonDataFromUrl(x)


#openFile = open('downloadedJsonFileOfHackathons.json')
#data = json.load(openFile)
#openFile.close()
#print(data)

#a = json.dump("foo",x)
#print(a)
#f = csv.writer(open("test.csv", "wb+"))

# Write CSV Header, If you dont need that, remove this line
#f.writerow(["pk", "model", "codename", "name", "content_type"])

#for x in x:
 #   f.writerow([x["pk"],
  #              x["model"],
   #             x["fields"]["codename"],
    #            x["fields"]["name"],
     #           x["fields"]["content_type"]])


 #   with urllib.request.urlopen("http://hackerleague.org/api/v1/hackathons.json?limit="+inputValue) as url:
#    hackerLeagueResponse = url.read()
#print(hackerLeagueResponse)