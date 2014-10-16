__author__ = 'stamse'
import urllib.request

with urllib.request.urlopen("http://hackerleague.org/api/v1/hackathons.json?limit=10&offset=1") as url:
    s = url.read()
#I'm guessing this would output the html source code?
#print(s)

import http.client

#api = curl http://hackerleague.org/api/v1/hackathons.json?limit=1&offset=1 | in2csv -f json -v > issues.csv

url = "http://hackerleague.org/api/v1/hackathons.json?limit=1&offset=1"
req = urllib.request.urlopen(url)
#req.add_header('Accept', 'application/json')
# make the request and print the results
#res = urllib.urlopen(req)
#print (res.read())

print(req)
#print("This is a new req:\n" + req)