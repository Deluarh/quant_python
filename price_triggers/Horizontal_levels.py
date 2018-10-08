# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 21:00:40 2018

@author: Phantom
"""




"""
максимум пишеться, если средняя скользящая возрастает, обратное спреведливо к мин
и максимум берерься не выше некого мат ожидания чтобы исключить ложные пробои 
можно искать уровни на истории цен, а не в текущем моменте чтобы удалить пробои(большая тень
и маленькое тело )

пишем в уровень красивое значение 5 или 0 ... мб масштаб округления будет зависить от цены

мб можно применять дляопределения стадии накопления
"""        
class Horizontal_levels: #горизонтальные уровни поддержки и сопротивления
    horizontal_levels =[]
    number_of_touches = []
    
    temp = []
    n_bar = 0
    def __init__(self, n):
        self.n_bar = n

    def go(self, putP):
        if len(self.temp) < self.n_bar:
            self.temp.append(putP)
            #self.calculate_MA()
            #return self.getMA()
        else: 
            self.temp.append(putP)
            self.temp.pop(0)
            self.calculate_levels()
            #return self.getMA()
    def calculate_levels(self):
        min(self.temp) 
        max(self.temp)
        if self.temp.index(min(self.temp), 0, 1) == 0:
            self.horizontal_levels.append(self.temp[0])
            print(self.horizontal_levels)
            #self.number_of_touches
        if self.temp.index(max(self.temp), 0, 1) == 0:
            self.horizontal_levels.append(self.temp[0])
            print(self.horizontal_levels)

