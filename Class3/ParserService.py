import socket
import sys
from inventario import Inventario
import json
#import threading
import signal  
import time
import traceback
cerrado=False
global timer

def handler(sig, frame):  # define the handler  
        global cerrado
        print('You pressed Ctrl+C!')
        traceback.print_stack(frame)
        cerrado = False
        
def main():
    global cerrado
    while cerrado == True:
        try: 
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            server_address = ('localhost', 4000)
            lista = p1.load_csv()
            dataAtx = json.dumps(lista)

            sent = sock.sendto(dataAtx.encode(encoding="utf-8"), server_address)
            print('waiting to receive')
            data, server = sock.recvfrom(4096)
            print('received {!r}'.format(data))
        finally:
            print('closing socket')
            sock.close()
        time.sleep(3)


#carga el directorio donde se va leer
cerrado = True
p1= Inventario()
# Create a UDP socket
signal.signal(signal.SIGINT, handler)
main()


