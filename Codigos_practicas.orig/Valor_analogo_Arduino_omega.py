import urllib
import ssl
import sys
import serial
import time
#Cambiar API_KEY por la clave de la plataforma
puerto=serial.Serial('/dev/ttyS1', baudrate=9600, timeout=1.0 )
url="https://api.thingspeak.com/update?api_key=API_KEY"

while True:
 linea=puerto.readline()
 f=urllib.urlopen(url+"&field1=%s"%(linea))
 print f.read()
 print url+"&field1=%s"%(linea)
 #print(linea) 
 time.sleep(15)
 
