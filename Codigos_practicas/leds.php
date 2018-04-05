<html>
 <head>
 <meta name="viewport" content="width=device-width" />
 <title>Control de Led</title>
 </head>
         <body>
         LED Control:
         <form method="get" action="leds.php">
                 <input type="submit" value="ON" name="on">
                 <input type="submit" value="OFF" name="off">
                 <input type="submit" value="BLINK" name="blink">
        </form>
         <?php
         $setmode17 = shell_exec("/usr/local/bin/gpio -g mode 4 out");
         if(isset($_GET['on'])){
                 $gpio_on = shell_exec("/usr/local/bin/gpio -g write 4 1");
                 echo "LED encendido";
         }
         else if(isset($_GET['off'])){
                 $gpio_off = shell_exec("/usr/local/bin/gpio -g write 4 0");
                 echo "LED apagado";
         }
          else if(isset($_GET['blink'])){
         echo "LED parpadeando";
         $gpio_on = shell_exec("/usr/local/bin/gpio -g write 4 1");
         sleep(1);
         $gpio_off = shell_exec("/usr/local/bin/gpio -g write 4 0");
         sleep(1);
         $gpio_on = shell_exec("/usr/local/bin/gpio -g write 4 1");
         sleep(1);
         $gpio_off = shell_exec("/usr/local/bin/gpio -g write 4 0");
}
         ?>
         </body>
 </html>
