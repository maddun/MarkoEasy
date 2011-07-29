# -*- coding: utf-8 -*-
# Файл содержащий класс для прямоугольников в которых будем менять координаты.
__author__ = 'comp124'

class MyRectangle :
    """ Класс для прямоугольников.
    """

    def  __init__(self, name ,x=0,y=0):
        """Консутруктор"""
        self.name = name
        self.x = x
        self.y = y


    def Move(self,x,y):
        """Сдвигает наш прямоугольник по координатам
        """
        self.x = x
        self.y = y




            


    