# -*- coding: utf-8 -*-
# Файл содержащий класс для прямоугольников в которых будем менять координаты.
__author__ = 'comp124'
from Client import SendMessage

class MyRectangle :
    """ Класс для прямоугольников.
    """

    def  __init__(self, name ,x = None,y=None):
        """Консутруктор"""
        if x == None :
            x = [0,0]
        if y == None:
            y = [1,1]
        self.name = name
        self.t1 = x
        self.t2 = y


    def Move(self,x,y):
        """Сдвигает наш прямоугольник по координатам
        """
        if x == 0 and y == 0:
            print "Сдвига нет!!"
        else:
            self.t1[0] += x
            self.t2[0] += x
            self.t1[1] += y
            self.t2[1] += y
            SendMessage(x,y)

    def MoveOnServ(self,x,y):
        """Сдвигает наш прямоугольник по координатам на серверной части (не посылает снова координаты)
        """
        if x == 0 and y == 0:
            print "Сдвига нет!!"
        else:
            self.t1[0] += x
            self.t2[0] += x
            self.t1[1] += y
            self.t2[1] += y
            print "Подвинул на сервере на %d по x и на %d по у" %(x,y)



            


    