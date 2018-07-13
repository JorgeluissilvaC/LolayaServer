# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 10:23:49 2018

@author: Ing Jorge Silva C
"""
import socket

def Main():
        host = '181.192.218.153'
        port = 4007
         
        mySocket = socket.socket()
        mySocket.connect((host,port))
         
        message = input(" -> ")
         
        while message != 'q':
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()
                 
                print ('Received from server: ' + data)
                 
                message = input(" -> ")
                 
        mySocket.close()
 
if __name__ == '__main__':
    Main()
