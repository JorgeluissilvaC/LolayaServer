# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 10:23:49 2018

@author: Ing Jorge Silva C
"""
import socket
import time

def Main():
        host = '127.0.0.1'
        port = 4007
         
        mySocket = socket.socket()
        mySocket.connect((host,port))
         
         
        while True:
                message = "ST300STT;109002241;08;1080;20180531;03:02:45;c2759;+10.903514;-074.797407;015.575;092.64;10;1;120;0.00;000000;1;0006;0000000012;4.1;0;0.00;0000;0000;0;0"
                mySocket.send(message.encode())
                time.sleep(10)
                message = "ST300ALT;109002241;08;1080;20180531;02:54:19;c2744;+10.903267;-074.797512;000.550;000.00;10;1;20;0.00;000000;5007;0000000010;4.1;1;0.00;0000;0000;0;0"
                mySocket.send(message.encode())
                time.sleep(10)
                message = "ST300ALT;109002241;08;1080;20180531;03:00:54;c2759;+10.903154;-074.797716;000.015;000.00;12;1;25;11.21;100000;6007;0000000010;4.1;0;0.00;0000;0000;0;0"
                mySocket.send(message.encode())
                time.sleep(10)
                message = "ST300EMG;109002241;08;1080;20180531;02:52:50;c2759;+10.903124;-074.797818;000.009;000.00;10;1;20;0.00;000000;3;0000000010;4.2;0;0.00;0000;0000;0;0"
                mySocket.send(message.encode())
                time.sleep(10)
                message = "ST300UEX;109002241;08;1080;20180531;07:41:56;2F100;+37.478519;+126.886819;000.012;000.00;9;1;0;15.30;001100;25;1;56;12;0;4.5;1"
                mySocket.send(message.encode())

                #data = mySocket.recv(1024).decode()
                time.sleep(10)
                print("Terminado")

        mySocket.close()

if __name__ == '__main__':
    Main()
