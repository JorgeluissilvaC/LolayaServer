# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 10:08:33 2018

@author: Ing Jorge Silva C
"""

#!/usr/bin/env python


from socket import socket, error
from threading import Thread
#import requests
# api-endpoint
URL = "http://127.0.0.1:8000/into/"


  
class Client(Thread):
    """
    Servidor eco - reenvía todo lo recibido.
    """
    
    def __init__(self, conn, addr):
        # Inicializar clase padre.
        Thread.__init__(self)
        
        self.conn = conn
        self.addr = addr
    
    def run(self):
        while True:
            try:
                # Recibir datos del cliente.
                input_data = self.conn.recv(1024)
            except error:
                print("[%s] Error de lectura." % self.name)
            else:
                # Reenviar la información recibida.
                if input_data:
                    #self.conn.send(input_data)
                    print(input_data)
                    # defining a params dict for the parameters to be sent to the API     
                    #requests.get(url = URL, params = {'q':input_data.decode()})
                    print("Información transmitida al server django")
def main():
    s = socket()
    
    # Escuchar peticiones en el puerto 4007.
    s.bind(("", 4007))
    s.listen(0)
    
    while True:
        conn, addr = s.accept()
        c = Client(conn, addr)
        c.start()
        print("%s:%d se ha conectado." % addr)


if __name__ == "__main__":
    main()
