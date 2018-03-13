import subprocess
import smtplib
import onionGpio
import time
from email.mime.text import MIMEText

pin1=onionGpio.OnionGpio(1)

status=pin1.setInputDirection()

#res=subprocess.check_output(["gpioctl","dirout","3"])
#res1=subprocess.check_output(["gpioctl","dirout-high","3"])

while True:
 value=pin1.getValue()

 #print(value)

 if int(value)==1:

  print("El switch esta en  ON, enviando email de alerta...")
  msg=MIMEText("La luz del cuarto esta encendida  ")
  
 else:
  print("El switch esta en OFF, enviando email de alerta...")
  msg=MIMEText("la luz del cuarto esta apagada ")


 server=smtplib.SMTP('smtp.gmail.com',587)
 server.starttls()
 server.login('claseiot@gmail.com','pregunte la clave a su profesor')
 msg['Subject']="Aviso de Iot Unipanamericana"
 server.sendmail("claseiot@gmail.com","correodestino@loquesea.com",msg.as_string())
 print("Email enviado")
 server.quit()
 time.sleep(60)
 
