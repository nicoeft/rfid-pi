#!/usr/bin/env python
# -*- coding: utf8 -*-
 
import RPi.GPIO as GPIO
from mfrc522 import MFRC522
import signal
import time

from app.utils.users import handle_event

continue_reading = True
 
# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()
 
# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)
 
# Create an object of the class MFRC522
MIFAREReader = MFRC522()
 
# Welcome message
print ("Welcome to the MFRC522 data read example")
print ("Press Ctrl-C to stop.")
 
# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
 
    # If a card is found
    if status == MIFAREReader.MI_OK:
        print ("Card detected")
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
 
    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        uuid_str = f"{uid[0]}-{uid[1]}-{uid[2]}-{uid[3]}-{uid[4]}"
        # Print UID
        print(f"Card read UID: {uuid_str}")
        
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)
        
        #Configure LED Output Pin
        GREEN_LED = 18
        
        GPIO.setup(GREEN_LED,GPIO.OUT)
        GPIO.output(GREEN_LED,GPIO.LOW)
        
        msg,success = handle_event(uuid_str, 1)
        led = GREEN_LED
        
        print(msg)
        GPIO.output(led, GPIO.HIGH)  # Turn on LED
        time.sleep(2)  # Wait 2 Seconds
        GPIO.output(led, GPIO.LOW)  # Turn off LED

        

