__author__ = 'stamse'

from urllib import request
import urllib.request
import json

#Ask user for number of Hackathons to be used for analysis
inputValue=input('Please enter the number of hackathons you want to analyze:')

print("You entered: " + inputValue)

#Call API as per the number of hackathons requested
targetUrl = ("http://hackerleague.org/api/v1/hackathons.json?limit="+inputValue)
print(targetUrl)

def downloadDataFromUrl(csv_url): #Our Main Fucntion for converting JSON to Formatted CSV
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_string = str(csv) #Converting to String
    lines = csv_string.split("\\n") #Making each entry on new line
    destination_url = "downloadedFileOf"+inputValue+"Hackathons.csv" #Hackathon quantity specific file name. Was going to use variety with offsets
    destination_url_txt = "downloadedFileOf"+inputValue+"Hackathons.txt" #Tested with text files as input to Tableau too.
    csvFileOpen = open(destination_url, "w")
    for line in lines:
        csvFileOpen.write(line + "\n")
    csvFileOpen.close()

    txtFileOpen = open(destination_url_txt, "w")
    for line in lines:
        txtFileOpen.write(line + "\n")
    txtFileOpen.close()

# Call the function to download data from the API Url
downloadDataFromUrl(targetUrl) #Download Live data from Hacker League Page

#The Stored file is pulled into Tableau Refresh Schedule by Running Windows script.(Tried successfully locally)

#todo:

#Post this CSV file on cloud storage so that Tableau can refresh from that
