# -*- coding: utf-8 -*-
__author__ = 'comp124'
import SocketServer
import threading
import sys
from WindowClass import Window
from Rectangle import MyRectangle
from PyQt4 import QtGui

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
        MyRectangle.Move(self.server.Window.square,int(incoming[0]),int(incoming[1]))
        self.server.Window.update()
        self.request.send(";".join([str(self.server.Window.square.x),str(self.server.Window.square.y)]))

class RectangleServer (SocketServer.TCPServer):
    """ Класс реализует сервер управляющий собственным прямоугольником и изменяющий координаты по сообщению клиента
    """
    def __init__(self, name):
        """ Инициализирует сервер. А также создает к нему собственное окно
        """
        SocketServer.TCPServer.__init__(self, ('localhost',11000),ServerRectHandler)
        self.Window = Window(name)

if   __name__ == '__main__':
    HOST, PORT = 'localhost', 11000
    ServAppl = QtGui.QApplication(sys.argv)
    MyServer = RectangleServer("Server")
    ServThread = threading.Thread(target=MyServer.serve_forever)
    ServThread.setDaemon(True)
    ServThread.start()
    MyServer.Window.show()
    sys.exit(ServAppl.exec_())

    
