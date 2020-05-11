import json
import requests


max_results = "1"
stop_id = "231291" # Broadale bus stop number
bus_number = "220"

response = requests.get(''.join(["https://data.smartdublin.ie/cgi-bin/rtpi/realtimebusinformation?format=json",\
	"&maxresults=", max_results, "&stopid=", stop_id, "&routeid=", bus_number]))

json_data = response.json()

data = ""
bus_count = int(json_data["numberofresults"])
for i in range(0,bus_count):
	route = json_data["results"][i]["route"]
	dueTime = json_data["results"][i]["duetime"]
	data += "%s is due at %s\n" % (route, dueTime)

print(data)