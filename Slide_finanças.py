import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from IPython.display import display

cotacao_ibov = web.DataReader('^BVSP', data_source='yahoo', start='2020-01-01', end='2020-11-10')
display(cotacao_ibov)
cotacao_ibov['Adj Close'].plot(figsize=(15, 5))

retorno_ibov = (cotacao_ibov['Adj Close'][-1] / cotacao_ibov['Adj Close'][0]) -1
print('Retorno de {:.2%}'.format(retorno_ibov))

#Média móvel da bolsa
cotacao_ibov['Adj Close'].plot(figsize=(10, 5), label='IBOV')
cotacao_ibov['Adj Close'].rolling(21).mean().plot(label='MM21')
cotacao_ibov['Adj Close'].rolling(34).mean().plot(label='MM34')

plt.legend()
plt.show()

carteira = pd.read_excel('Carteira.xlsx')
display(carteira)

cotacoes_carteira = pd.DataFrame()

cotacoes_carteira = web.DataReader('BOVA11.SA', data_source='yahoo', start='2020-01-01', end='2020-11-10')
display(cotacoes_carteira)

extracao = web.DataReader('BOVA11.SA', data_source='yahoo', start='2020-01-01', end='2020-11-10')
cotacoes_carteira['BOVA11.SA'] = extracao['Adj Close']
display(cotacoes_carteira)

cotacoes_carteira = pd.DataFrame()

for ativo in carteira['Ativos']:
    extracao = web.DataReader('{}.SA'.format(ativo), data_source='yahoo', start='2020-01-01', end='2020-11-10')
    cotacoes_carteira[ativo] = extracao['Adj Close']

display(cotacoes_carteira)

cotacoes_carteira.info()

cotacoes_carteira = cotacoes_carteira.ffill()
cotacoes_carteira.info()

carteira_norm = cotacoes_carteira / cotacoes_carteira.iloc[0]
carteira_norm.plot(figsize=(15, 5))
plt.legend(loc='upper left')

cotacao_ibov = web.DataReader('^BVSP', data_source='yahoo', start='2020-01-01', end='2020-11-10')
display(cotacao_ibov)

valor_investido = pd.DataFrame()

for ativo in carteira['Ativos']:
    valor_investido[ativo] = cotacoes_carteira[ativo] * carteira.loc[carteira['Ativos']==ativo, 'Qtde'].values[0]
display(valor_investido)

valor_investido['Total'] = valor_investido.sum(axis=1)

valor_investido_norm = valor_investido / valor_investido.iloc[0]
cotacao_ibov_norm = cotacao_ibov / cotacao_ibov.iloc[0]

valor_investido_norm['Total'].plot(figsize=(15, 5), label='Carteira')
cotacao_ibov_norm['Adj.Close'].plot(label='IBOV')
plt.legend()
plt.show()