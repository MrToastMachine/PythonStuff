import json
import requests
# from pprint import pprint
from tkinter import *
 
def clicked():
	# lbl.configure(text="Button was clicked !!")
	window.destroy()


# Get Dublin Bus information
stopID = "182"
response = requests.get(''.join(["https://data.smartdublin.ie/cgi-bin/rtpi/realtimebusinformation?stopid=",\
	stopID,"&format=json"]))
json_data = response.json()

# Build a string with the retrieved information
# pprint(json_data)
data = ""
bus_count = int(json_data["numberofresults"])
for i in range(0,bus_count):
	route = json_data["results"][i]["route"]
	dueTime = json_data["results"][i]["duetime"]
	data += "%s is due in %s minutes\n" % (route, dueTime)
	# print "%s is due in %s minutes" % (route, dueTime)

# Set up the user interface window
window = Tk()
window.title("Dublin Bus times")
# window.geometry('350x200')
 
lbl = Label(window, text=data, font=("Arial", 20))
lbl.grid(column=0, row=0)

btn = Button(window, text="Close", command=clicked)
btn.grid(column=0, row=1)
 
window.mainloop()