# -*- coding: utf-8 -*-
__author__ = 'comp124'

import socket

def SendMessage (x,y):
    data = ";".join([str(x),str(y)])
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost',11000))
    sock.send(data)
    recive = sock.recv(1024)
    #print "Answer from server: %s" %recive
    print "Сервер говорит координаты", recive.split(";")[:2], recive.split(";")[2:]
    sock.close
    