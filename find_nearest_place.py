import urllib.request
import json
from dist_two_points import distance 
#def printresults(data):
    #Downloading .json file
 #   theJSON = json.loads(data)
    #Finding cases with more than 1000 reports
  #  for i in theJSON["features"]:
   #     if not i["properties"]["felt"] is None and i["properties"]["felt"] > 1000:
    #        print(i["properties"]["felt"], i["properties"]["mag"], i["properties"]["place"], datetime.fromtimestamp(i["properties"]["time"] // 1000))
    #Printing coordinates of all Earthquakes 
    #for i in theJSON["features"]:
     #   print(i["geometry"]["coordinates"])
def nearest(latitude, longitude):
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
    webUrl = urllib.request.urlopen(urlData)
    if webUrl.getcode() == 200:
        res = webUrl.read()
    data = json.loads(res)
    ans = None
    dist = 10 ** 100
    for case in data["features"]:
        cur_dist =  distance(latitude,longitude,case["geometry"]["coordinates"][1],case["geometry"]["coordinates"][0])
        if cur_dist < dist:
            dist = cur_dist
            ans = case
    return f"The nearest earthquake was {int(dist)} KM from you in this place: " + ans["properties"]["place"]
    





