# -*- coding: utf-8 -*-
__author__ = 'comp124'

import SocketServer
from Server import ServerRectHandler
from  Rectangle import MyRectangle
import sys
from PyQt4 import QtGui


if __name__ == '__main__':
    Rec1 = MyRectangle("SquareClient",[2,3],[3,4])
    x = int(raw_input("Ввеедите смещение по X: \n"))
    y = int(raw_input("Ввеедите смещение по Y: \n"))
    Rec1.Move(x,y)