import requests
import paho.mqtt.client as mqtt
import time
location="Bogota"
api_key=""
#lat=4.6209279
#lon=-74.0742169
url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(location, api_key)
#url="https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid={}".format(lat,lon,api_key)
print(url)
try:
	while True:
		r = requests.get(url)
		info=r.json()
		print(info)
		temp=info['main']['temp']
		hum=info['main']['humidity']
		sensacion_t=info['main']['feels_like']
		v_viento=info['wind']['speed']
		print(temp,hum,sensacion_t,v_viento)
		broker_url = "IP"
		broker_port = 1883
		client = mqtt.Client()
		client.connect(broker_url, broker_port)
		client.subscribe([("bogota/temperatura",0),("bogota/humedad",0),("bogota/sensacion_t",0),("bogota/viento",0)], qos=1)
		client.publish(topic="bogota/temperatura", payload=temp, qos=1, retain=False)
		client.publish(topic="bogota/humedad", payload=hum, qos=1, retain=False)
		client.publish(topic="bogota/sensacion_t", payload=sensacion_t, qos=1, retain=False)
		client.publish(topic="bogota/viento", payload=v_viento, qos=1, retain=False)
		client.connect(broker_url, broker_port)
		
		time.sleep(1)
except KeyboardInterrupt:
	pass
client.loop_stop()
client.disconnect()



