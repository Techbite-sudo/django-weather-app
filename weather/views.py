from django.shortcuts import render
import urllib
import json

# Create your views here.
def index(request):
    if request.method == "POST":
        if "city" in request.POST:
            city = request.POST["city"]
            res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()
        else:
            city = ""
            
    return render(request, "index.html", {})
