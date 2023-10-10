import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Obter dados de preços de uma ação específica
ticker = 'AAPL'
dados = yf.download(ticker, start='2022-01-01', end='2022-12-31')

#print(dados.head())

# Calcular a média móvel de 50 dias

dados['MA50'] = dados['Close'].rolling(window=50).mean()

#Plotar gráficos de preços e média móvel
plt.figure(figsize=(10,6))
plt.plot(dados['Close'], label='Preço de Fechamento')
plt.plot(dados['MA50'], label='Média Móvel 50 dias', color='red')
plt.legend()
plt.title('Preço de Fechamento e Média Móvel de 50 dias para AAPL')
plt.xlabel('Data')
plt.ylabel('Preço')
#plt.show()

# Exemplo de uma estratégia simples de cruzamento de médias móveis

import backtrader as bt

class EstrategiaCruzamento(bt.Strategy):
    params = (('periodo_curto', 50), ('periodo_longo', 200))

    def __init__(self):
        self.media_curta = bt.indicators.SimpleMovingAverage(self.data,period=self.params.periodo_curto)
        self.media_longa = bt.indicators.SimpleMovingAverage(self.data,period=self.params.periodo_longo)

    def next(self):
        if self.media_curta > self.media_longa:
            self.buy()
        elif self.media_curta < self.media_longa:
            self.sell()

cerebro = bt.Cerebro()
cerebro.addstrategy(EstrategiaCruzamento)

dados = bt.feeds.YahooFinanceData(dataname='AAPL',fromdate='2022-01-01',todate='2022-12-31')
cerebro.adddata(dados)

cerebro.run()
cerebro.plot()
