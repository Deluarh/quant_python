# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 20:47:25 2018

@author: Phantom
"""
import algorithm_result
import Data             
test_data = Data.MyData('C:\\Users\\Phantom\\Downloads\\GAZP_170620_180620.csv').detData() 
#TICKER, PER, DATE, TIME, OPEN, HIGH, LOW, CLOSE, VOL


strategyN = 2
if strategyN == 1: # пересечение цены средней скользящей (реверсивная стратегия)
    import trend_following.MA
    import algorithm_result
    ma1 = trend_following.MA.MA(200)
    test = algorithm_result.Test()
    for i in test_data:
        #print('________________________')
        #print(float(i[7]))
        ma = ma1.setMA( float(i[7]))
        #print ( ma)
        if float(i[7]) > ma:
            test.buy(float(i[7]))
        else:
            test.sell(float(i[7]))
    test.show()
    print("конец")
       
if strategyN == 2:# реверсивные простые MA
    import trend_following.MA
    import algorithm_result
    maS = trend_following.MA.MA(9)
    maL = trend_following.MA.MA(26)
    test = algorithm_result.Test()
    mark_bs = 0 # 0 - начало работы, 1 - в покупке, -1 -в продаже
    for i in test_data:
       # print('________________________')
        current_maS = maS.setMA( float(i[7]))
        current_maL = maL.setMA( float(i[7]))
        #print(current_maS)
        #print(current_maL)
        if current_maS > current_maL:
            test.buy(float(i[7]))
            pass # покупка
        if current_maS < current_maL:
            test.sell(float(i[7])) #продажа
    test.show()
    print("конец")
            
"""            
if strategyN == 3: #горизонтальные уровни
    level = Horizontal_levels(50)
    for i in test_data:
        print('________________________')
        level.go(float(i[7]))
        #print(float(i[7]))
        #print(ma1.setMA( float(i[7])))
"""        
if strategyN == 4: #RSI
    import return_to_average.RSI
    rsi_test = return_to_average.RSI.RSI()
    test = algorithm_result.Test()
    minimym = 30
    maximym = 70
    for i in test_data:
        #print('________________________')
        rsi_test.go(float(i[7]))
        if rsi_test.getCurrentRSI() > maximym:
            test.sell(float(i[7])) #продажа
        if rsi_test.getCurrentRSI() < minimym:
            test.buy(float(i[7]))
        
        #print(min(min_max))
        #print(max(min_max))
        #print(float(i[7]))
        #print(ma1.setMA( float(i[7])))
    test.show()
    print("конец")
if strategyN == 5: #3 скользящие средние 
    """покупка при S>M>L закрытие при M>S>L"""
    import trend_following.MA
    import algorithm_result
    maS = trend_following.MA.MA(9)
    maM = trend_following.MA.MA(26)
    maL = trend_following.MA.MA(52)
    test = algorithm_result.Test()
    mark_temp = 0
    for i in test_data:
        #print('________________________')
        L = maL.setMA(float(i[7]))
        M = maM.setMA(float(i[7]))
        S = maS.setMA(float(i[7]))
        if mark_temp == 0:
            if S > M and M > L: #S>M>L
                test.buy(float(i[7]))
                mark_temp = 1
            if S < M and M < L: #S<M<L
                test.sell(float(i[7])) #продажа
                mark_temp = 1
            
        #выход из сделки
        if mark_temp != 0:
            if S > M and S < L: # M<S<L
                test.buy(float(i[7]))
                mark_temp = 0
            if S < M and S > L: #M>S>L
                test.sell(float(i[7])) #продажа
                mark_temp = 0
    test.show()
    print("конец")