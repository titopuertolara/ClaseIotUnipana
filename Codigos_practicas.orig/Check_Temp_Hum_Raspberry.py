import Adafruit_DHT
import math
import ssl
import sys
import time
import urllib
sensor=Adafruit_DHT.DHT11
#Cambiar API_KEY por la clave generada en la plataforma
pin=2

baseUrl="https://api.thingspeak.com/update?api_key=API_KEY"
while True:
  hum ,temp =Adafruit_DHT.read_retry(sensor,pin)
  f=urllib.urlopen(baseUrl+"&field1=%s&field2=%s"%(temp,hum))
  print f.read()
  print baseUrl+"&field1=%s&field2=%s"%(temp,hum) 
  f.close()

time.sleep(25) 
