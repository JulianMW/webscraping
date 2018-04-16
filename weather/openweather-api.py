import requests
import json

key = ''   # api key
fullurl = 'http://api.openweathermap.org/data/2.5/weather?id=' + _id + '&APPID=' + key   # full url
fullurl = 'http://api.openweathermap.org/data/2.5/weather?lat=43.65&lon=-79.38&APPID='
# lat=43.65&lon=-79.38 corresponds to downtown toronto

r = requests.get(fullurl)

json_data = r.json()

maximum_temperature = json_data['main']['temp_max']
print(json.dumps(json_data, indent=4, sort_keys=True))
