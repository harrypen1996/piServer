#!/usr/bin/python3

import _thread, time, socket

data = ''   # Declare an empty variable
# UDP setup for listening
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 12345))  # I'm using port 12345 to bind to

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


while 1:
    print ('Now I can do something useful while waiting in the main body.')
    if data:
        print ('THE PACKET RECEIVED BY THE MAIN BODY IS: ' + data)
        data = ''   # Empty the variable ready for the next one
    time.sleep(2)