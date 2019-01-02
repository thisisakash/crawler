import requests

r = requests.get('http://knit.ac.in/')

print (r.status_code)

print (r.headers)

print (r.encoding)