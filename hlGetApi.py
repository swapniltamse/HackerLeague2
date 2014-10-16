__author__ = 'stamse'

import urllib
import http.client

conn =http.client.HTTPSConnection("fisheye")
conn.connect()
r2 = conn.getresponse()
print (r1,r2.status,r2.reason,r2)
r3=r2.read()
print(r3)
r4=str(r3)
print (r4)
data = XML(r4).find("token").text
print (data)
# data1=urllib.quote_plus(data, safe=":")
# print data1
args=urllib.urlencode({'FEAUTH':data}).replace("%3A", ":")
print ("args is", args)
#args={}
req = conn.request("get","/rest-service/reviews-v1")
r3 = conn.getresponse()
status = r3.status
print ("the url is")#, r3.getheader('Location')
url=r3.getheader('location', '')
print (url)
url1=r3.msg#.dict['location']
print (url1)
#print req.url
#print req.get_method()
print (dir(req)) # list lots of other stuff in Request
print ("after sending open review request")
print (r3)
print (req,r3.status,r3.reason,r3)
r4=r3.read()
print(r4)
r5=str(r4)
print (r5)
# json_ob=json.loads(r3.read())
# print json_ob