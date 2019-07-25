import RPi.GPIO as GPIO
import os
import sys
from subprocess import Popen
import time
from time import sleep
import urllib 
import urllib2


#BUTTONS ACTIVITIES
def movie1(channel):
    print("Button #1 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/1-beebot.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=1')

def movie2(channel):
    print("Button #2 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/2-bluebot.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=2')

def movie3(channel):
    print("Button #3 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/3-dashdot.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=3')

def movie4(channel):
    print("Button #4 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/4-ozobot-bit.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=4')

def movie5(channel):
    print("Button #5 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/5-ozobot-evo.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=5')

def movie6(channel):
    print("Button #6 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/6-makey.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=6')

def movie7(channel):
    print("Button #7 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/7-edison.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=7')

def movie8(channel):
    print("Button #8 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/8-edcreate.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=8')

def movie9(channel):
    print("Button #9 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/9-sphero.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=9')

def movie10(channel):
    print("Button #10 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/10-littlebits.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=10')

def movie11(channel):
    print("Button #11 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/11-vex.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=11')

def movie12(channel):
    print("Button #12 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/12-microbit.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=12')

def movie13(channel):
    print("Button #13 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/13-lego-ev3.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=13')

def movie14(channel):
    print("Button #14 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/14-lego-wedo.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=14')

def movie15(channel):
    print("Button #15 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/15-arduino.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=15')

def movie16(channel):
    print("Button #16 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/17-bare-conductive.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=16')

def movie17(channel):
    print("Button #17 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/makerbuino.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=17')

def movie18(channel):
    print("Button #18 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/raspberry-pi.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=18')

def movie19(channel):
    print("Button #19 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/19-engino.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=19')

def movie20(channel):
    print("Button #20 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/20-truckbots.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=20')

def movie21(channel):
    print("Button #21 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/21-alpha.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=21')

def movie22(channel):
    print("Button #22 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/22-pololu-balancer.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=22')

def movie23(channel):
    print("Button #23 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/23-hexapod.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=23')

def movie24(channel):
    print("Button #24 was pushed!")
    os.system('killall omxplayer.bin')
    #omxc = Popen(['omxplayer', '-b', movie1])
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/24-uarm.mp4"])
    sleep(1)

    # Sending the data to thingspeak
    response = urllib2.urlopen('https://api.thingspeak.com/update?api_key=H3LMV95MN0K3AGQC&field1=24')

def close_all(channel):
    print("Closing all!")
    os.system('killall omxplayer.bin')


try:
    #delay before start
    sleep(5)

    # Setting GPIO layout
    GPIO.setmode(GPIO.BOARD)

    # Set pin as input pin pulled down to GND
    GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 1
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 2
    GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 3

    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 4
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 5
    GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 6

    GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 7
    GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 8
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 9

    GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 10
    GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 11
    GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 12
    GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 13
    GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 14

    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 15

    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 16
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 17

    GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 18
    GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 19
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 20

    GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 21

    GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 22
    GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 23
    GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Button 24

    #GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #close all

    #play video at start
    sleep(1)
    os.system('killall omxplayer.bin')
    sleep(1)
    Popen(['omxplayer', '-b', '--loop', "/home/pi/Videos/clips/24-uarm.mp4"])
    sleep(1)

    while True:
        if not 'event' in locals():
            event = GPIO.add_event_detect(3, GPIO.RISING, callback=movie1, bouncetime=200)
            event = GPIO.add_event_detect(5, GPIO.RISING, callback=movie2, bouncetime=200)
            event = GPIO.add_event_detect(7, GPIO.RISING, callback=movie3, bouncetime=200)
            event = GPIO.add_event_detect(11, GPIO.RISING, callback=movie4, bouncetime=200)
            event = GPIO.add_event_detect(13, GPIO.RISING, callback=movie5, bouncetime=200)
            event = GPIO.add_event_detect(15, GPIO.RISING, callback=movie6, bouncetime=200)
            event = GPIO.add_event_detect(19, GPIO.RISING, callback=movie7, bouncetime=200)
            event = GPIO.add_event_detect(21, GPIO.RISING, callback=movie8, bouncetime=200)
            event = GPIO.add_event_detect(23, GPIO.RISING, callback=movie9, bouncetime=200)
            event = GPIO.add_event_detect(29, GPIO.RISING, callback=movie10, bouncetime=200)
            event = GPIO.add_event_detect(31, GPIO.RISING, callback=movie11, bouncetime=200)
            event = GPIO.add_event_detect(33, GPIO.RISING, callback=movie12, bouncetime=200)
            event = GPIO.add_event_detect(35, GPIO.RISING, callback=movie13, bouncetime=200)
            event = GPIO.add_event_detect(37, GPIO.RISING, callback=movie14, bouncetime=200)
            event = GPIO.add_event_detect(12, GPIO.RISING, callback=movie15, bouncetime=200)
            event = GPIO.add_event_detect(16, GPIO.RISING, callback=movie16, bouncetime=200)
            event = GPIO.add_event_detect(18, GPIO.RISING, callback=movie17, bouncetime=200)
            event = GPIO.add_event_detect(22, GPIO.RISING, callback=movie18, bouncetime=200)
            event = GPIO.add_event_detect(8, GPIO.RISING, callback=movie19, bouncetime=200)
            event = GPIO.add_event_detect(10, GPIO.RISING, callback=movie20, bouncetime=200)
            event = GPIO.add_event_detect(32, GPIO.RISING, callback=movie21, bouncetime=200)
            event = GPIO.add_event_detect(36, GPIO.RISING, callback=movie22, bouncetime=200)
            event = GPIO.add_event_detect(38, GPIO.RISING, callback=movie23, bouncetime=200)
            event = GPIO.add_event_detect(40, GPIO.RISING, callback=movie24, bouncetime=200)


            #event = GPIO.add_event_detect(29, GPIO.RISING, callback=close_all, bouncetime=200)

        else:
            time.sleep(1)

finally:  
    GPIO.cleanup()
