# -*- coding: utf-8 -*-
__author__ = 'comp124'

import SocketServer
from Server import ServerRectHandler
from  Rectangle import MyRectangle
import sys
from PyQt4 import QtGui


if __name__ == '__main__':
    Rec1 = MyRectangle("Squa1reClient",[2,3],[3,4])
    #Rec1.Move(1,3)
    app = QtGui.QApplication(sys.argv)
    wiget = QtGui.QWidget()
    wiget.setWindowTitle("Server")
    wiget.show()
    x = int(raw_input("Ввеедите смещение по X: \n"))
    y = int(raw_input("Ввеедите смещение по Y: \n"))
    Rec1.Move(x,y)
    sys.exit(app.exec_())