import socket
import sys
from inventario import inventario
import json
import threading

def func():
    try:
        lista = p1.load_csv()
        dataAtx = json.dumps(lista)

        sent = sock.sendto(dataAtx.encode(encoding="utf-8"), server_address)
        print('waiting to receive')
        data, server = sock.recvfrom(4096)
        print('received {!r}'.format(data))
        global timer
        timer = threading.Timer(3, func)
        timer.start()
    finally:
        print('closing socket')
        #sock.close()

#carga el directorio donde se va leer
p1= inventario()
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 4000)
func()


