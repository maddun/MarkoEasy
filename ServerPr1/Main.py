# -*- coding: utf-8 -*-
__author__ = 'comp124'

import SocketServer
from Server import ServerRectHandler
from  Rectangle import MyRectangle
import sys
from PyQt4 import QtGui, QtCore

class ClientWindow (QtGui.QWidget):
    """ Класс для окна клиента
    """
    def __init__(self, parent = None):
        """ Переопределение инстанса.
        """
        QtGui.QWidget.__init__(self, parent)
        self.square = MyRectangle("SquareClient",[2,3],[3,4])
        self.resize(120,120)
        self.setWindowTitle("Client")
        

if __name__ == '__main__':
    ClientAppl = QtGui.QApplication(sys.argv)
    ClientWind = ClientWindow()
    ClientWind.show()
    Rec1 = MyRectangle("SquareClient",[2,3],[3,4])
    x = int(raw_input("Ввеедите смещение по X: \n"))
    y = int(raw_input("Ввеедите смещение по Y: \n"))
    Rec1.Move(x,y)
    sys.exit(ClientAppl.exec_())