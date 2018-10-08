# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 21:21:10 2018

@author: Phantom

import application_in_quik
t = application_in_quik.Application()
t.new_order(self, price, quantity, operation, typeT, classcode,seccode)

"""

class Application:
    ACCOUNT = 'L01-00000F00'#'MC0139600000'
    CLIENT_CODE = 'L01-00000F00'#'OPEN51487'
    TRANS_ID = 1
    #очистка файлов    
    
    def new_order(self, price, quantity, operation, typeT, classcode,seccode):
        account_client = 'ACCOUNT=' + str(self.ACCOUNT) + '; CLIENT_CODE=' +str(self.CLIENT_CODE) + ';'
        characteristics_deal = 'TYPE='+str(typeT)+'; TRANS_ID='+str(self.TRANS_ID)+'; CLASSCODE='+str(classcode)+'; SECCODE='+str(seccode)+'; ACTION=NEW_ORDER;'
        self.TRANS_ID +=1
        deal = 'OPERATION='+str(operation)+'; PRICE='+str(price)+'; QUANTITY='+str(quantity)+';'
        toFile = account_client + characteristics_deal + deal
        print(toFile)
        wFile = open('C:\\Users\\Phantom\\My_Progect\\quant\\TRANS\\trans_options.tri', 'a')
        wFile.write(toFile + '\n')
        wFile.close()
    
    def doc_clean(self):
        open('C:\\Users\\Phantom\\My_Progect\\quant\\TRANS\\Journal.trr', 'w').close() 
        open('C:\\Users\\Phantom\\My_Progect\\quant\\TRANS\\result.tro', 'w').close()
        open('C:\\Users\\Phantom\\My_Progect\\quant\\TRANS\\trans_options.tri', 'w').close()


"""
Файл представляет собой последовательность строк, каждая из которых 
содержит информацию по отдельной транзакции. Параметры транзакции 
описываются в виде «НАЗВАНИЕ_ПАРАМЕТРА=значение_параметра» и разделяются символом «;».

Параметры и принимаемые ими значения:
Параметр
Значение
CLASSCODE - Код класса, по которому выполняется транзакция, например EQBR.
SECCODE - Код инструмента, по которому выполняется транзакция, например RU0008943394
ACTION - Вид транзакции, имеющий одно из следующих значений: 
            NEW_ORDER - новая заявка,
                NEW_NEG_DEAL - новая заявка на внебиржевую сделку,
            NEW_STOP_ORDER - новая стоп-заявка,
            KILL_ORDER - снять заявку,
                KILL_NEG_DEAL - снять заявку на внебиржевую сделку,
            KILL_STOP_ORDER - снять стоп-заявку.
ACCOUNT - номер счета Трейдера, обязательный параметр
CLIENT_CODE - 12-ти символьный код клиента, необязательный параметр
TYPE - Тип заявки, необязательный параметр. Возможные значения: 
            L – лимитированная,
            M – рыночная. 
OPERATION - Направление заявки, обязательный параметр. Возможные значения: 
        S – продать, 
        B – купить.
PRICE - Цена заявки, за единицу инструмента. Обязательный параметр. 
STOPPRICE - Стоп-цена, за единицу инструмента. Используется только при ACTION=NEW_STOP_ORDER
QUANTITY - Количество лотов в заявке, обязательный параметр
PARTNER - Код организации – партнера по внебиржевой сделке Применяется только при ACTION=NEW_NEG_ORDER
ORDER_KEY - Номер заявки, снимаемой из торговой системы
            Применяется при ACTION=KILL_ORDER или ACTION=KILL_NEG_DEAL
STOP_ORER_KEY - Номер стоп-заявки, снимаемой из торговой системы
                Применяется только при ACTION=KILL_STOP_ORDER
TRANS_ID - Уникальный идентификационный номер заявки
SETTLE_CODE -Код расчетов при исполнении внебиржевых заявок
PRICE2 - Цена второй части РЕПО
REPORATE - Ставка РЕПО, в процентах 
REFUNDRATE - Ставка фиксированного возмещения, выплачиваемого в случае неисполнения второй части РЕПО, в процентах

Примеры строк, которые могут содержаться в файле:
Транзакция
Строка
Заявка на продажу 
(Ростелеком, лимитированная, 3 лота по 253.3 руб.)
ACCOUNT=NL0058900043; CLIENT_CODE=467; TYPE=L; TRANS_ID=1; CLASSCODE=EQBR; SECCODE=RU0008943394; ACTION=NEW_ORDER; OPERATION=S; PRICE=43,21; QUANTITY=3;
Заявка на покупку 
(ЛУКОЙЛ, лимитированная, 3 лота по 253.3 руб.)
ACCOUNT=NL0058900043; CLIENT_CODE=467; TYPE=L; TRANS_ID=2; CLASSCODE=EQBR; SECCODE=RU0009024277; ACTION=NEW_ORDER; OPERATION=B; PRICE=253,3; QUANTITY=3;
Снятие заявки с номером 503983
CLASSCODE=EQBR; SECCODE=RU0009024277; TRANS_ID=5; ACTION=KILL_ORDER; ORDER_KEY=503983;
Снятие внебиржевой заявки с номером 503984
CLASSCODE=EQBR; TRANS_ID=6; ACTION=KILL_NEG_DEAL; ORDER_KEY=503984;

    """