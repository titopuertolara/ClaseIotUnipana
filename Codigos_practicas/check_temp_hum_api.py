#import Adafruit_DHT
import math
import ssl
import sys
import time
import urllib.request
import random
import requests
location="Tunja"
api_key="846b0dceddfc94408e12502aad4a2a68"
#lat=4.6209279
#lon=-74.0742169
url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(location, api_key)
#url="https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid={}".format(lat,lon,api_key)
#sensor=Adafruit_DHT.DHT11
#Cambiar API_KEY por la clave generada en la plataforma
pin=2

baseUrl="https://api.thingspeak.com/update?api_key=P818G98UMJY7FT0D"
while True:
  #hum ,temp =Adafruit_DHT.read_retry(sensor,pin)

  #hum,temp=round(10*random.random()),round(20*random.random())
  r = requests.get(url) #traer datos
  
  info=r.json()
  #print(info)
  thermal_sens=info['main']['feels_like']
  temp=info['main']['temp']
  hum=info['main']['humidity']
  f=urllib.request.urlopen(baseUrl+"&field1=%s&field2=%s&field3=%s"%(temp,hum,thermal_sens))#enviar datos
  print(f.read())
  print(baseUrl+"&field1=%s&field2=%s&field3=%s"%(temp,hum,thermal_sens))
  f.close()

time.sleep(25) 
