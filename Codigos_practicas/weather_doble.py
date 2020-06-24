import requests
import paho.mqtt.client as mqtt
import time
location="melgar"
api_key="846b0dceddfc94408e12502aad4a2a68"
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
		broker_url = "25.119.63.148"
		broker_port = 1883
		client = mqtt.Client()
		client.connect(broker_url, broker_port)
		client.subscribe([("bogota/temperatura",0),("bogota/humedad",0),("bogota/sensacion_t",0),("bogota/viento",0)], qos=1)
		client.publish(topic="bogota/temperatura", payload=temp, qos=1, retain=False)
		client.publish(topic="bogota/humedad", payload=hum, qos=1, retain=False)
		client.publish(topic="bogota/sensacion_t", payload=sensacion_t, qos=1, retain=False)
		client.publish(topic="bogota/viento", payload=v_viento, qos=1, retain=False)
		client.connect(broker_url, broker_port)
		lorena=mqtt.Client()
		lorena_ip="25.10.73.181"
		lorena.connect(lorena_ip,broker_port)
		lorena.subscribe([("bogota/temperatura",0),("bogota/humedad",0),("bogota/sensacion_t",0),("bogota/viento",0)], qos=1)
		lorena.publish(topic="bogota/temperatura", payload=temp, qos=1, retain=False)
		lorena.publish(topic="bogota/humedad", payload=hum, qos=1, retain=False)
		lorena.publish(topic="bogota/sensacion_t", payload=sensacion_t, qos=1, retain=False)
		lorena.publish(topic="bogota/viento", payload=v_viento, qos=1, retain=False)

		time.sleep(1)
except KeyboardInterrupt:
	pass
client.loop_stop()
client.disconnect()



