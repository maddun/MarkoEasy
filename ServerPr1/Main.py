# -*- coding: utf-8 -*-
__author__ = 'comp124'

import sys
from WindowClass import ClientWindow
from PyQt4 import QtGui


if __name__ == '__main__':
    ClientAppl = QtGui.QApplication(sys.argv)
    ClientWind = ClientWindow("Client")
    ClientWind.show()
    sys.exit(ClientAppl.exec_())