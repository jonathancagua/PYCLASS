import socket
import sys
from inventario import Inventario
import json
import threading
import signal  
import time
import traceback
cerrado=False
global timer

def handler(sig, frame):  # define the handler  
        print('You pressed Ctrl+C!')
        global cerrado
        traceback.print_stack(frame)
        #sys.exit(0)
        cerrado = True
        #sys.exit(0)
        
def main():
    try:
        global cerrado
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = ('localhost', 4000)
        lista = p1.load_csv()
        dataAtx = json.dumps(lista)

        sent = sock.sendto(dataAtx.encode(encoding="utf-8"), server_address)
        print('waiting to receive')
        data, server = sock.recvfrom(4096)
        print('received {!r}'.format(data))
       
        if cerrado == False:
            timer = threading.Timer(3, func)
            timer.start()
        
    finally:
        print('closing socket')
        sock.close()
        if cerrado == True:
            sys.exit(0)

#carga el directorio donde se va leer
cerrado = False
p1= Inventario()
# Create a UDP socket
signal.signal(signal.SIGINT, handler)
main()


