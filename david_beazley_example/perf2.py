# Time of a long running request


import time

from threading import Thread
from socket import *


sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('', 25000))

n = 0

def monitor():
    global n
    while True:
        time.sleep(1)
        print(n, "req / sec")
        n = 0

Thread(target=monitor).start()

while True:
    """
        Run this program with smaller value in the .send function
        and also run nc localhost 25000 with higher fibonacci value.
        you will see the no. of connections per second would be dropped.
    """
    sock.send(b'3') # If you increase this value, It will affect the 
                    # total no. of connections per second.
    resp = sock.recv(100)
    n += 1

