# Fibonacci Microservice

from socket import *
from fib import fib
from threading import Thread
from concurrent.futures import ProcessPoolExecutor as Pool

pool = Pool(4)

def fib_handler(client):
    while True:
        # try:
            req = client.recv(100)
            if not req:
                break
            n = int(req)
            future = pool.submit(fib, n)
            result = future.result()
            resp = str(result).encode('ascii') + b'\n'
            client.send(resp)
        # except Exception as e:
        #     print("Error:", e)
        #     break
    print("Connection Closed")

def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    print("Server listening on", address)
    while True:
        client, addr = sock.accept()
        print("Connection", addr)
        Thread(target=fib_handler, args=(client,)).start()

if __name__ == "__main__":
    fib_server(('', 25000))