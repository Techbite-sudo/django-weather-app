from django.shortcuts import render
import urllib
import json


# Create your views here.
def index(request):
    city = ""  # Initialize the variable outside the if statement
    data = {}

    if request.method == "POST":
        if "city" in request.POST:
            city = request.POST["city"]
            res = urllib.request.urlopen(
                "http://api.openweathermap.org/data/2.5/weather?q="
                + city
                + "&appid=199cf6ab32b9b546f1e8309d13b5cf09"
            ).read()
            json_data = json.loads(res)
            print(json)
            data = {
                "country_code": str(json_data["sys"]["country"]),
                "coordinate": str(json_data["coord"]["lon"])
                + " "
                + str(json_data["coord"]["lat"]),
                "temp": str(json_data["main"]["temp"]) + "k",
                "pressure": str(json_data["main"]["pressure"]),
                "humidity": str(json_data["main"]["humidity"]),
            }

    return render(request, "index.html", {"city": city, "data": data})
