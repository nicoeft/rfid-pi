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

DEFAULT_PROVIDER_ID = 1
print("RFID Payment System Demo")
print("Press Ctrl-C to stop.")
 
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
 
    # If a card is found
    if status == MIFAREReader.MI_OK:
        print("RFID tag detected")

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
 
    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        print("--------------")
        uuid_str = f"{uid[0]}-{uid[1]}-{uid[2]}-{uid[3]}-{uid[4]}"
        # Print UID
        print(f"Tag read UID: {uuid_str}")
        
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)
        msg,success = handle_event(uuid_str, DEFAULT_PROVIDER_ID)
        print(msg)
        print("--------------")

        

