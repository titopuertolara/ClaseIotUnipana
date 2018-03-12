import subprocess
import urllib
import ssl
import sys
import time
import math
#Cambiar API_KEY por la clave generada en la plataforma
baseUrl="https://api.thingspeak.com/update?api_key=API_KEY"

while True:
 res=subprocess.check_output(["./checkHumidity","19","DHT11"])


 reslist = res.strip().split("\n")

 temp=reslist[1]
 hum=reslist[0]
 f=urllib.urlopen(baseUrl+"&field1=%s&field2=%s"%(temp,hum))
 print f.read()
 print baseUrl+"&field1=%s&field2=%s"%(temp,hum)
 f.close()
 time.sleep(15)
