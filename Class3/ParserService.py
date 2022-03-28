import socket
import sys
from inventario import Inventario
import json
import signal  
import time

class ServiceExit(Exception):
    """
    Custom exception which is used to trigger the clean exit
    of all running threads and the main program.
    """
    print('Saliendo')
    pass


class Main:     
    def handler(self, sig, frame):  # define the handler  
        print('You pressed Ctrl+C!')
        raise ServiceExit()

    def main(self):
        signal.signal(signal.SIGINT, self.handler)
        if [] == p1.load_csv():
            print("Revisar archivos de configuracion")
        else:
            try: 
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                server_address = ('localhost', 4000)
                while True:
                    lista = p1.load_csv()
                    dataAtx = json.dumps(lista)
                    sent = sock.sendto(dataAtx.encode(encoding="utf-8"), server_address)
                    print('waiting to receive')
                    data, server = sock.recvfrom(4096)
                    print('received {!r}'.format(data))
                    time.sleep(3)
            except ServiceExit:
                sock.close()
                print('closing socket')
                print("ServiceExit")
                exit() 
            
            




#carga el directorio donde se va leer
p1= Inventario()
# Create main service
m = Main()
m.main()


