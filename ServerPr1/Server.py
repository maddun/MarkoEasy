# -*- coding: utf-8 -*-
__author__ = 'comp124'
import SocketServer
import threading
import sys
from Rectangle import MyRectangle
from PyQt4 import QtGui, QtCore, uic

class ServerRectHandler (SocketServer.BaseRequestHandler):
    """Обрабатывает сообщения отправлеяемые клиентом.
       перегружает метод handle()
    """

    def handle(self):
        """ Получает сообщение и изменяет на полученные в сообщении координаты прямоугольника
        """
        self.data = self.request.recv(1024).strip()
        incoming = self.data.split(";")
        #Двигаем на сервере по полученным координатам
        MyRectangle.MoveOnServ(self.server.R1,int(incoming[0]),int(incoming[1]))
        print "Координаты %s" %self.data
        print "Теперь координаты у сервера", self.server.R1.t1, "и", self.server.R1.t2
        #Отсылаем координаты на клиент
        self.request.send(";".join([str(self.server.R1.t1[0]),str(self.server.R1.t1[1]),str(self.server.R1.t2[0]),str(self.server.R1.t2[1])]))

class RectangleServer (SocketServer.TCPServer):
    """ Класс реализует сервер управляющий собственным прямоугольником и изменяющий координаты по сообщению клиента
    """
    def __init__(self, name):
        """ Инициализирует сервер. А также создает к нему прямоугольник
        """
        self.R1 = MyRectangle(name)
        SocketServer.TCPServer.__init__(self, ('localhost',11000),ServerRectHandler)

    def Starter(self):
       """ Запускает сервер.
       """
       #ServThread = threading.Thread(target=MyServer.serve_forever)
       #ServThread.setDaemon(True)
       #print "Is server thread alive",ServThread.isAlive()
       ServThread.start()
       #print "Is server thread alive",ServThread.isAlive()

    def Stopper(self):
       """ Останавливает сервер.
       """
       #ServThread = threading.Thread(target=MyServer.serve_forever)
       #ServThread.setDaemon(True)
       #print "Is server thread alive",ServThread.isAlive()
       self.shutdown()
       #print "Is server thread alive",ServThread.isAlive()


class ServerWindow (QtGui.QWidget):
    """
       Класс для окошка сервера.
    """
    def __init__(self,Server,parent = None):
        """ Создаем собственное окошко
        """
        QtGui.QWidget.__init__(self,parent)
        self.resize(150,90)
        self.setWindowTitle('Server')
        StartButton = QtGui.QPushButton('Start',self)
        StartButton.setGeometry(10, 10, 60, 35)
        #StopButton = QtGui.QPushButton('Stop',self)
        #StopButton.setGeometry(80, 10, 60, 35)
        self.connect(StartButton,QtCore.SIGNAL('clicked()'),Server.Starter)
        #self.connect(StopButton,QtCore.SIGNAL('clicked()'),Server.Stopper)

    def closeEvent(self, QCloseEvent):
        MyServer.shutdown()
        print "Server shutting down!!"
        print "Server thread is a live", ServThread.isAlive()
        QCloseEvent.accept()


if   __name__ == '__main__':
    HOST, PORT = 'localhost', 11000
    MyServer = RectangleServer("ServSquare")
    #print "Запускаю сервер!"
    ServThread = threading.Thread(target=MyServer.serve_forever)
    ServAppl = QtGui.QApplication(sys.argv)
    ServWindow = ServerWindow(MyServer)
    #ServWindow = QtGui.QWidget()
    #uic.loadUi("MainWind.ui",ServWindow)
    ServWindow.show()
    #MyServer.shutdown()
    sys.exit(ServAppl.exec_())

    
