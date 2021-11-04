import urllib.request
import json
from datetime import datetime

def printresults(data):
    #Downloading .json file
    theJSON = json.loads(data)
    #Finding cases with more than 1000 reports
    for i in theJSON["features"]:
        if not i["properties"]["felt"] is None and i["properties"]["felt"] > 1000:
            print(i["properties"]["felt"], i["properties"]["mag"], i["properties"]["place"], datetime.fromtimestamp(i["properties"]["time"] // 1000))
    #Printing coordinates of all Earthquakes 
    for i in theJSON["features"]:
        print(i["geometry"]["coordinates"])

urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
#Access request
webUrl = urllib.request.urlopen(urlData)
if webUrl.getcode() == 200:
    #Reading of the file
    res = webUrl.read()
    printresults(res)
