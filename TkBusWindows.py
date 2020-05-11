import json
import requests

from tkinter import *

import os


def clicked():
	# lbl.configure(text="Button was clicked !!")
	window.destroy()

# Get Bus Eireann bus information
max_results = "1"
stop_id = "231291" # Broadale bus stop number
bus_number = "220"

response = requests.get(''.join(["https://data.smartdublin.ie/cgi-bin/rtpi/realtimebusinformation?format=json",\
	"&maxresults=", max_results, "&stopid=", stop_id, "&routeid=", bus_number]))
	
json_data = response.json()

# Build a string with the retrieved information
data = ""
bus_count = int(json_data["numberofresults"])
for i in range(0,bus_count):
	route = json_data["results"][i]["route"]
	dueTime = json_data["results"][i]["duetime"]
	data += "%s is due at %s\n" % (route, dueTime)

window = Tk()
window.title("Cork Buses")
#window.geometry('350x250')

lbl = Label(window, text=data, font=("Arial", 20))
lbl.grid(column=0, row=0)

btn = Button(window, text="Close", command=clicked)
btn.grid(column=0, row=1)

window.mainloop()


print(data)
print("Done")