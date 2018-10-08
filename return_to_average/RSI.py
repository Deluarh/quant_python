# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 21:06:46 2018

@author: Phantom
"""
import trend_following.MA as MA
class RSI: #индекс относительной силы, используют свойство рынка возвращаться к среднему
    """
    Большинство трейдеров считают рынок переку-
    пленным, если RSI превышает 70, и перепроданным, если RSI меньше 30.
    
    индекса RSI Уайлдера всегда используются 9 или 14 периодов.
    """
    n_bar = 14 # закрытие этих периодов
    rsi_arry = []
    curRSI = 50
    def getCurrentRSI(self):
        return self.curRSI
    
    def go(self, curP):
        if len(self.rsi_arry) < self.n_bar:
            self.rsi_arry.append(curP)
            return self.getCurrentRSI()
        else: 
            self.rsi_arry.append(curP)
            self.rsi_arry.pop(0)
            self.calculate_RSI()
            return self.getCurrentRSI() 
    def calculate_RSI(self):
        self.curRSI = 100 - 100/(1 + self.curRS())
        if self.curRS() == -1:
            print(self.curRS())
        #RSI = 100 – 100/(1 + RS)
    
    def curRS(self):
        upMA = MA.MA(self.n_bar)
        downMA = MA.MA(self.n_bar)
        temp_i = self.rsi_arry[0]# предыдущеезначение i-1
        for i in range( 1, len(self.rsi_arry)):
            if self.rsi_arry[i] > temp_i:
                upMA.setMA( (self.rsi_arry[i] - temp_i))
                temp_i = self.rsi_arry[i] 
            else:
                downMA.setMA( (temp_i - self.rsi_arry[i]))
                temp_i = self.rsi_arry[i]
        if downMA.getMA() ==0:
            return
        ###
        '''
        print('!!!!!')
        print (upMA.getMA() / downMA.getMA())
        print(upMA.getMA())
        print(downMA.getMA())'''
        return (upMA.getMA() / downMA.getMA())
        #RS (14) = Σ(Положительные приросты цены)/Σ(|Отрицательные приросты цены|)
        """
        RSI = 100 – 100 / 1 + RS,

где Среднее за Х дней, когда рынок закрывался ростом
Среднее за Х дней, когда рынок закрывался снижением
RS = .

При расчете индекса RSI чаще всего используются 14 периодов, на-
пример дней или недель. Для определения среднего значения роста вы-
числяется сумма положительных изменений цены в пунктах за 14 дней,

которая делится на 14. Для определения среднего значения снижения
вычисляется сумма отрицательных изменений цены в пунктах, которая

затем делится на 1415. Большинство трейдеров считают рынок переку-
пленным, если RSI превышает 70, и перепроданным, если RSI меньше 30."""