#!/usr/bin/python3

import _thread, time, socket
from PyP100 import PyL530

wave = False
l530 = PyL530.L530("192.168.1.232", "harrs@btinternet.com", "davsha123") #Creating a L530 bulb object

l530.handshake() #Creates the cookies required for further methods
l530.login() #Sends credentials to the plug and creates AES Key and IV for further methods

#All the bulbs have the PyP100 functions and additionally allows for setting brightness, colour and white temperature

data = ''   # Declare an empty variable
# UDP setup for listening
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 6968))  # I'm using port 12345 to bind to

# Define a function for the thread
def listening_thread():
    global data     # data needs to be defined as global inside the thread
    while True:
        data_raw, addr = sock.recvfrom(1024)
        data = data_raw.decode()    # My test message is encoded
        print ("Received message inside thread:", data)

try:
   _thread.start_new_thread(listening_thread, ())
except:
    print ("Error: unable to start thread")
    quit()


def DimAndOff():
    l530.setBrightness(100)   
    l530.setBrightness(95)   
    l530.setBrightness(90)   
    l530.setBrightness(85)   
    l530.setBrightness(80)   
    l530.setBrightness(85)   
    l530.setBrightness(80)   
    l530.setBrightness(75)   
    l530.setBrightness(70)   
    l530.setBrightness(65)
    l530.setBrightness(60)   
    l530.setBrightness(55)   
    l530.setBrightness(50)   
    l530.setBrightness(45)   
    l530.setBrightness(40)   
    l530.setBrightness(35)   
    l530.setBrightness(30)   
    l530.setBrightness(25)   
    l530.setBrightness(20)   
    l530.setBrightness(15)
    l530.setBrightness(10)
    l530.setBrightness(5)          
    l530.turnOff()

while True:
    if data:
        print ('Received:' + data)
        print ('Executing...')
        exec(data)
        data = ''   # Empty the variable ready for the next one
    time.sleep(1)
