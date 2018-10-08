# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 21:14:04 2018

@author: Phantom
"""
        
class Test:
    commission = 0.57 #комиссия %
    slippage = 0   #проскальзывание
    buy_arry =[] 
    sell_arry = []
    
    profitable_trades = []
    losing_trades = []

    def sell(self, price):        
        if  len(self.buy_arry) < len(self.sell_arry):
            return
        else:
            self.sell_arry.append( price ) #закрытие покупки
            #print("sell")
        
    def buy(self, price):        
        if len(self.buy_arry) > len(self.sell_arry):
            return 0
        if len(self.buy_arry) == len(self.sell_arry):#buy
            self.buy_arry.append(price)
            #print("buy 1")
            return 1
        else:
            self.buy_arry.append( - price) #закрытие короткой покупки
            #print("buy close")
            return 1

    def show(self):
        print("комиссия = ", self.commission, " %")
        print("проскальзывание = ", self.slippage)
        print("=== ")
        if len(self.buy_arry) == len(self.sell_arry):
            print('')
        elif len(self.buy_arry) > len(self.sell_arry):
            self.buy_arry.pop(-1)
        else:
            self.sell_arry.pop(-1)
        
        profit_buy = []
        profit_sell = []
        for i in range (0, len(self.buy_arry) ):
            if self.buy_arry[i] > 0:
                temp = self.sell_arry[i] - self.buy_arry[i]
                temp = temp - (temp * self.commission / 100)
                profit_buy.append(temp)
            else:
                temp = self.sell_arry[i] + self.buy_arry[i]
                temp = temp - (temp * self.commission / 100)
                profit_sell.append(temp)
            
        quantity_of_deals = len(self.buy_arry)
        print("кол закрытых сделок = ", quantity_of_deals) 
        
        number_of_profitable_trades = 0
        total_net_profit = 0
        for i in profit_buy:
            if i > 0:
                number_of_profitable_trades += 1
                total_net_profit +=i
        for i in profit_sell:
            if i > 0:
                number_of_profitable_trades += 1
                total_net_profit +=i
                
            
        print("кол прибыльных сделок = ", number_of_profitable_trades)
        w_profit = number_of_profitable_trades / quantity_of_deals
        print("доля прибыльных сделок = ", w_profit)
        print("совокупная чистая прибыль = ", total_net_profit)
        maximum_drawdown = 0 # максимальная просадка
        temp_maximum_drawdown1 = min(profit_buy)
        temp_maximum_drawdown2 = min(profit_sell)
        if temp_maximum_drawdown1 < temp_maximum_drawdown2:
            maximum_drawdown = temp_maximum_drawdown1
        else:
            maximum_drawdown = temp_maximum_drawdown2
        print("Максимальный убыток = ", maximum_drawdown)
        print("""максимальное количество последовательных убыточных сделок (MCL)  """)
        
"""
3. Число дней показывает средний срок существования сделки.
Как и с числом сделок, при прочих равных условиях, чем меньше
срок существования сделки, даже демонстрирующей высокие ре-
зультаты, тем лучше.
Единственное, на что следует обращать внимание здесь, это какая
система используется — система следования за трендом или воз-
врата к среднему . В случае следования за трендом большее число
дней приводит обычно к получению более значительной прибыли.

4. Максимальный размер просадки (макс. просадка) характеризует
наибольшую просадку за период тестирования. Он определяет тре-
бования к абсолютному минимальному капиталу в торговой систе-
ме. (Благоразумное управление денежными средствами предпола-
гает запас не менее 50% сверх исторически наихудшей просадки ;
более детально этот вопрос рассмотрен в главе 8.)
Большинство создателей систем включают в свои таблицы также
колонку «Максимальный убыток», в которой отражается наиболь-
ший убыток на сделку. Хотя при благоразумном управлении цено-
вым риском максимальный убыток на сделку не должен превышать
1–2% от совокупных средств на счете, этот показатель не учитыва-
ет корреляцию активов в портфеле (см. главу 8).
Поскольку одна из главных идей настоящей книги — это сокраще-
ние риска через диверсификацию путем включения в портфель не-
коррелирующих классов активов и/или активов с отрицательной
корреляцией (см. главу 9), мне представляется, что максимальный
убыток на сделку может вводить в заблуждение и, таким образом,
является менее эффективным показателем по сравнению с макси-
мальным размером просадки по средствам . Если по каким-либо
причинам (например, отсутствие капитала, корпоративные огра-
ничения) диверсифицированный портфель активов не может быть
сформирован, то включение показателя максимального убытка
и следование правилу 1–2% являются абсолютно необходимыми.

5. Максимальная длительность просадки (MDD) характеризует наи-
большую продолжительность просадки по средствам до достиже-
ния нового максимума. Этот показатель принципиально важен

для психологической подготовки к периоду ожидания нового пика.



7. Отношение прибыли к максимальной просадке (P:MD) — это ве-
личина, получаемая делением средней прибыли на максимальную
просадку. Чем выше это отношение, тем лучше. Это, пожалуй, са-
мое важное поле в таблице, поскольку оно позволяет оценивать
прибыль относительно риска, связанного с ее получением.


8. Отношение прибыли к убыткам (P:L) — это величина, получаемая
делением средней прибыли на средний убыток. Как и в случае
с отношением P:MD, чем выше P:L, тем лучше. Системы следо-
вания за трендом должны иметь очень хорошее отношение P:L,
поскольку они обычно отражают небольшой процент прибыль-
ных сделок. Это означает, что крупные прибыли и незначитель-
ные убытки являются ключевым условием получения хорошего
значения P:L. Размер этих отношений падает в системах возврата
к среднему , однако процент прибыльных сделок должен компен-
сировать это падение.


10. Процент времени (Время %) показывает, какую часть времени си-
стема имеет открытую позицию на рынке. При равных значениях
остальных полей более низкий процент времени предпочтителен,
поскольку доступный капитал остается связанным менее продол-
жительное время для генерирования той же доходности.
"""