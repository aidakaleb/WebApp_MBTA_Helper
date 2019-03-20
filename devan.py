import urllib.request
import json
from pprint import pprint

#Mapquest

MAPQUEST_API_KEY = 'F2ZiIvn03ZurvGBryY5eag3rouzW9WaG'
# MAPINPUT1 = (input(str('please input your city')))


def find(MAPINPUT1):
    MAPINPUT1 = MAPINPUT1.replace(" ", "+")
    url = "http://www.mapquestapi.com/geocoding/v1/address?key={}&location={},MA".format(MAPQUEST_API_KEY, MAPINPUT1)
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    pprint(response_data)
    LatLng = (response_data["results"][0]["locations"][0]["displayLatLng"])
    print('The Latitude Is: ',LatLng.get("lat"))
    print('The Longitude Is: ',LatLng.get("lng"))
    print(url)



    #MBTA

    MBTA_API_KEY = '7ad2915d10f34026bc93eaef8dd9198f'
    latitude = LatLng.get('lat')
    longitude = LatLng.get('lng')
    url2 = "https://api-v3.mbta.com/stops?api_key={}&filter[latitude]={}&filter[longitude]={}&sort=distance".format(MBTA_API_KEY, latitude, longitude)
    print(url2)
    y = urllib.request.urlopen(url2)
    response_text2 = y.read().decode('utf-8')
    response_data_2 = json.loads(response_text2)
    pprint(response_data_2)
    Stop_Name = (response_data_2['data'][0]["attributes"]['name'])
    print(Stop_Name)
    Wheelchair_accessible = (response_data_2['data'][0]["attributes"]['wheelchair_boarding'])
    print('The Closest Stop To You is: ',Stop_Name)
    if Wheelchair_accessible == 1:
        print('Wheelchairs Accepted')
    elif Wheelchair_accessible == 2:
        print('Wheelchairs Not Accepted')
    else:
        print("No Information Found")

    #GOOGLE MAPS
    SEARCHINPUT = 'MBTA%20stop%20near%20'+Stop_Name.replace(' ', '%20')
    GAPIKEY = 'AIzaSyCDLTn0Slx13crZWXxkXKHlTZxWys45X5U'
    GURL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={}&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key={}".format(SEARCHINPUT, GAPIKEY)
    print(GURL)
    h = urllib.request.urlopen(GURL)
    response_text3 = h.read().decode('utf-8')
    response_data_3 = json.loads(response_text3)
    pprint(response_data_3)
    Rating = (response_data_3['candidates'][0]['rating'])
    print(Rating)

    return Stop_Name, Wheelchair_accessible, Rating