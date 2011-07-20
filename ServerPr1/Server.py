# -*- coding: utf-8 -*-
__author__ = 'comp124'
import SocketServer
from Rectangle import MyRectangle

class ServerRectHandler (SocketServer.BaseRequestHandler):
    """Обрабатывает сообщения отправлеяемые клиентом.
       перегружает метод handle()
    """

    def handle(self):
        """ Получает сообщение и изменяет на полученные в сообщении координаты прямоугольника
        """
        self.data = self.request.recv(1024).strip()
        incoming = self.data.split(";")
        MyRectangle.MoveOnServ(R1,int(incoming[0]),int(incoming[1]))
        #print "Координаты %s" %self.data
        print "Теперь координаты у сервера", R1.t1, "и", R1.t2
        self.request.send(";".join([str(R1.t1[0]),str(R1.t1[1]),str(R1.t2[0]),str(R1.t2[1])]))

        

if   __name__ == '__main__':
    HOST, PORT = 'localhost', 11000
    R1 = MyRectangle("ServerSquare")
    MyServer = SocketServer.TCPServer((HOST,PORT),ServerRectHandler)
    print "Запускаю сервер!"
    MyServer.serve_forever()