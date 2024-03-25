import requests
import sys

city_name = sys.argv

def getweather(C):
    url = "https://wttr.in/{}".format(C)
    try:
        data = requests.get(url)
        T = data.text
    except:
        T = "Fake city. :/"
    return T
print(getweather(city_name))
