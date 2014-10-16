__author__ = 'stamse'

from urllib import request
import urllib.request
import json
#jsonDownload = json.dumps("http://hackerleague.org/api/v1/hackathons.json?limit=1")
#print(jsonDownload)


inputValue=input('Please enter the number of hackathons you want to analyze:')

print("You entered: " + inputValue)

targetUrl = ("http://hackerleague.org/api/v1/hackathons.json?limit="+inputValue)
print(targetUrl)

targetUrl2 = ("http://hackerleague.org/api/v1/hackathons.json?limit=6")
print(targetUrl2)

def downloadDataFromUrl(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_string = str(csv)
    lines = csv_string.split("\\n")
    destination_url = "downloadedFileOf"+inputValue+"Hackathons.csv"
    destination_url_txt = "downloadedFileOf"+inputValue+"Hackathons.txt"
    csvFileOpen = open(destination_url, "w")
    for line in lines:
        csvFileOpen.write(line + "\n")
    csvFileOpen.close()

    txtFileOpen = open(destination_url_txt, "w")
    for line in lines:
        txtFileOpen.write(line + "\n")
    txtFileOpen.close()

# Call the function to download data from the API Url
downloadDataFromUrl(targetUrl)


def downloadHlData(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_string = str(csv)
    lines = csv_string.split("\\n")
    destination_url = "downloadedFileOfHackathonsData.csv"
    fileOpen = open(destination_url, "w")
    for line in lines:
        fileOpen.write(line + "\n")
    fileOpen.close()
downloadHlData(targetUrl2)


#Send inputValue to hacker league api
#url = "http://hackerleague.org/api/v1/hackathons.json?limit=1&offset=1"
# Get JSON from hacker league API
__author__ = 'stamse'
