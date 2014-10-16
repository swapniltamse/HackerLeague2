__author__ = 'stamse'
import urllib.request
import json

x = "http://hackerleague.org/api/v1/hackathons.json?limit=1"
y = urllib.request.urlopen(x)
z = y.read()

print (y)

#This is the required JSON
print (z)

#NowToConvert this to CSV

file = open (data.csv)
csv_file = csv.writer(file)
