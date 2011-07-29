# -*- coding: utf-8 -*-
__author__ = 'comp124'

from PyQt4 import QtGui, QtCore
from Rectangle import MyRectangle
from Network import SendMessage

class Window(QtGui.QWidget):
    """ Класс окно для клиента и сервера
    """
    def __init__(self,WindName,parent = None):
        """ Создаем собственное окошко
        """
        QtGui.QWidget.__init__(self,parent)
        self.resize(150,120)
        self.setWindowTitle(WindName)
        self.square = MyRectangle(WindName)

    def paintEvent(self, QPaintEvent):
        """ Перегружаем перерисовку
        """
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

    def drawRectangles(self, qp):
        """ Рисуем прямоугольник с координатами из квадрата, хранящегося в окне
        """
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)
        qp.setBrush(QtGui.QColor(255, 0, 0, 80))
        qp.drawRect(self.square.x, self.square.y, 90, 90)


    def mouseMoveEvent(self, QMouseEvent):
        """ Перегружаем обработчик движения мыши с нажатой клавишей
        """
        #Необходимо перерисовать для начала собственный квадрат
        self.square.Move(QMouseEvent.pos().x(), QMouseEvent.pos().y())
        self.update()
        #Затем послать данные на сервер
        #SendMessage(QMouseEvent.pos().x(),QMouseEvent.pos().y())

    def mouseReleaseEvent(self, QMouseEvent):
        """ Перегружаем обработчик для отпускания мыши
        """
        self.square.Move(QMouseEvent.pos().x(), QMouseEvent.pos().y())
        self.update()

class ClientWindow(Window):
    """ Класс для окна клиента
    """
    def mouseMoveEvent(self, QMouseEvent):
        """ Перегружаем обработчик движения мыши с нажатой клавишей
        """
        #Необходимо перерисовать для начала собственный квадрат
        self.square.Move(QMouseEvent.pos().x(), QMouseEvent.pos().y())
        self.update()
        #Затем послать данные на сервер
        SendMessage(QMouseEvent.pos().x(),QMouseEvent.pos().y())

    def mouseReleaseEvent(self, QMouseEvent):
        """ Перегружаем обработчик для отпускания мыши
        """
        self.square.Move(QMouseEvent.pos().x(), QMouseEvent.pos().y())
        self.update()
        SendMessage(QMouseEvent.pos().x(),QMouseEvent.pos().y())