__author__ = 'stamse'
template = "<html><body><h1>Hello %s!</h1></body></html>"
print template % "Reader"
<html><body><h1>Hello Reader</h1></body></html>

from string import Template
template = Template("<html><body><h1>Hello ${name}</h1></body></html>")
print template.substitute(dict(name='Dinsdale'))
<html><body><h1>Hello Dinsdale</h1></body></html>