#!/usr/bin/python3
#
#

import urllib3
import re
import requests
import json


## Get IP ##
OPENER = urllib3.PoolManager()
OPENER.addheaders = [('User-agent', 'Mozilla/5.0')]
MY_IP = OPENER.request('GET', 'http://httpbin.org/ip')
IP = json.loads(MY_IP.data.decode('utf-8'))
IP = IP['origin']
print("IP Address: %s" % IP)


## Get GeoLOCation - Country ##
GEO_LO = requests.get('http://ipinfo.io/%s/country' % IP)
LOC = (GEO_LO.content).decode('UTF-8').rstrip()
print("Country: %s" % LOC)

## Get GeoLOCation - City ##
GEO_CITY = requests.get('http://ipinfo.io/%s/city' % IP)
CITY = (GEO_CITY.content).decode('UTF-8').rstrip()
print("City: %s" % CITY)       

## Get GeoLOCation - Region ##
GEO_REGION = requests.get('http://ipinfo.io/%s/region' % IP)
REGION = (GEO_REGION.content).decode('UTF-8').rstrip()
print("Region: %s" % REGION)
