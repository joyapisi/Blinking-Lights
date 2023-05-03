import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #make button an input
GPIO.setup(22,GPIO.OUT) # Make first LED connected to Pin 22 an Output
GPIO.setup(18,GPIO.OUT) # Make second LED connected to Pin 18 an Output

while  True:                  # Create a Loop
        button = GPIO.input(23)
        if GPIO.input(23)==0:            # If button is pressed
            GPIO.output(22,GPIO.HIGH) 
            GPIO.output(18,GPIO.HIGH) 
            print ("Button Was Pressed:")
            print ("Button turned your lights on")
            time.sleep(1)
            
         else:                        
            GPIO.output(22,GPIO.LOW) # Turn LED off
            GPIO.output(18,GPIO.LOW) # Turn LED off
            print ("LEDs turned off")
             
GPIO.cleanup()