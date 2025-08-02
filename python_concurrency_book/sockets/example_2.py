# handling multiple connections from sockets

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)
server_socket.listen()

connections = []

try:
    while True:
        
        connection, client_address = server_socket.accept()
        print(f"I have got connection from {client_address}")
        connections.append(connection) #appending clients in a collection
        
        # loop over all connection to extract the data
        for connection in connections:
    
            buffer = b''
            
            while buffer[-2:] != b'\r\n':
                data = connection.recv(2)
                if not data:
                    break
                else:
                    print(f"I got data: {data}")
                    buffer = buffer + data
    
            print(f"All buffer data: {buffer}")
    
            # sending data back to client
            connection.sendall(buffer)
    
finally:
    server_socket.close()
