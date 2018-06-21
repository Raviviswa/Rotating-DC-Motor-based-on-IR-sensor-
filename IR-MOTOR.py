import Rpi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

Motor = 16
Led = 8
IR = 10

GPIO.setup(Motor,GPIO.OUT)
GPIO.setup(Led,GPIO.OUT)
GPIO.setup(IR,GPIO.IN)

if(GPIO.input(10)==1):
    print("Turning on the Motor")
    GPIO.output(Motor,GPIO.HIGH)
    GPIO.output(Led,GPIO.HIGH)
else:
    Print ("no object detected")
    GPIO.output(Motor,GPIO.LOW)
    GPIO.output(Led,GPIO.LOW)
GPIO.cleanup()
