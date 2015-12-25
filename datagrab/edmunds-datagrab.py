#!/usr/bin/env python
# https://api.edmunds.com/api/vehicle/v2/engines/{id}?fmt=json&api_key={api key}


import urllib2
import json

edmunds_api = "k3tfz63cnad848vumgfwpn36"
makes_url = "http://api.edmunds.com/api/vehicle/v2/makes?fmt=json&api_key=k3tfz63cnad848vumgfwpn36"

makes_json_obj = urllib2.urlopen(makes_url)
makes_json = json.load(makes_json_obj)

for item in makes_json['makes']:
	print item['name']
	print item['models'][0]['id']
