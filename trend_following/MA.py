# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 20:42:24 2018

@author: Phantom
"""
#Линейное взвешивание и экспоненциальное сглаживание скользящих средних
#адаптивной скользящей средней c волатильностью
# ma с объемами
#объемозависимая скользящая средняя.
class MA: # простая скользящая средняя
    N = 0
    currentMA =0
    ma_arry = []
    def __init__(self, n):
        self.N = n    
    def getMA(self):
        return self.currentMA
    def setMA(self, curP):
        if len(self.ma_arry) < self.N:
            self.ma_arry.append(curP)
            self.calculate_MA()
            return self.getMA()
        else: 
            self.ma_arry.append(curP)
            self.ma_arry.pop(0)
            self.calculate_MA()
            return self.getMA()      
    def calculate_MA(self):
        current = 0.0
        for i in self.ma_arry:
            current += i
        self.currentMA = current / len(self.ma_arry)