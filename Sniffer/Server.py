# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 10:08:33 2018

@author: Ing Jorge Silva C
"""

#!/usr/bin/env python


from socket import socket, error
from threading import Thread
import requests
# api-endpoint
URL = "http://181.192.218.153:4006/into/"

  
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
                break
            else:
                # Reenviar la información recibida.
                if input_data:
                    self.conn.send(input_data)
                    print(input_data.decode())
                    # defining a params dict for the parameters to be sent to the API     
                    #requests.get(url = URL, params = {'q':input_data.decode()})
                    #print("Información transmitida al server")
def main():
    s = socket()
    
    # Escuchar peticiones en el puerto 6030.
    s.bind(("", 4007))
    s.listen(0)
    
    while True:
        conn, addr = s.accept()
        c = Client(conn, addr)
        c.start()
        print("%s:%d se ha conectado." % addr)


if __name__ == "__main__":
    main()


"""

import socket 
import sys 
import threading
from queue import Queue

NUMERO_DE_HILOS= 2
JOB_NUMBER = [1,2]
queue = Queue()
ALL_CONNECTIONS =[]
ALL_ADDRESSES = []


def socket_create():
    try:
        global host
        global port
        global s
        
        host = ''
        port = 4007
        s = socket.socket()
    except socket.error as msg:
        print("Socket  create Error " + str(msg))

# Enlazar con el cliente y escuchar el puerto

def socket_blind():
    try:
        global host
        global port
        global s
        print("Enlazando socket al puerto: "+ str(port))
        s.bind((host,port))
        s.listen(100)
    except socket.error as msg:
         print("Socket Binding Error " + str(msg) + ".  Reintentando... ")
         socket_blind()
         
# Establecer una conección con un cliente

def socket_accept():
    con, addr = s.accept()
    print("Establecida con " +"IP: "+ addr[0]+" Port: "+ str(addr[1]))
    send_commands(con) 
    con.close()
#Aceptar con de multiples plientes y enviarlo a una lista. 

def accept_connections():
    for c in ALL_CONNECTIONS:
        c.close
        pass
    del ALL_CONNECTIONS[:]
    del ALL_ADDRESSES[:]
    while 1:
        try: 
            con, addr = s.accept()
            con.setblocking(1)
            ALL_CONNECTIONS.append(con)
            ALL_ADDRESSES.append(addr)
            print("Establecida con " +"IP: "+ addr[0]+" Port: "+ str(addr[1]))
        except socket.error as msg:
            print("Socket Conectando Error " + str(msg) )
            
            
    
def send_commands(con):
    while True:
        cmd = input()
        if cmd=='quitar':
            con.close
            s.close
            sys.exit()
        if len(str.encode(cmd))>0:
            con.send(str.encode(cmd))
            client_respose = str(con.recv(1024),"utf-8")
            print("Respuesta del cliente: " + client_respose)
            
def main():
    socket_create()
    socket_blind()
    accept_connections()  
main()


"""