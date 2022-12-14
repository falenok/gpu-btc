# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1twl_DTZrcEJRmECYQH0d0JJzY0TYrr4p
"""

import pandas as pd
import numpy as n
import matplotlib.pyplot as plt
import seaborn as sns

"""Загрузка данных"""

df_n_3070_8gb = pd.read_csv('/content/df_n_3070_8gb.csv', index_col='date')
df_n_2070_8gb = pd.read_csv('/content/df_n_2070_8gb.csv', index_col='date')
df_a_5700_8gb = pd.read_csv('/content/df_a_5700_8gb.csv', index_col='date')
df_a_580_8gb = pd.read_csv('/content/df_a_580_8gb.csv', index_col='date')
df_a_radeon_VII_16gb = pd.read_csv('/content/df_a_radeon_VII_16gb.csv', index_col='date')

df_n_3070_8gb.drop(['Unnamed: 0'], axis=1, inplace=True)
df_n_2070_8gb.drop(['Unnamed: 0'], axis=1, inplace=True)
df_a_5700_8gb.drop(['Unnamed: 0'], axis=1, inplace=True)
df_a_580_8gb.drop(['Unnamed: 0'], axis=1, inplace=True)
df_a_radeon_VII_16gb.drop(['Unnamed: 0'], axis=1, inplace=True)

df_n_3070_8gb = df_n_3070_8gb.rename(columns = {'y' : 'n_3070_8gb'})
df_n_2070_8gb = df_n_2070_8gb.rename(columns = {'y' : 'n_2070_8gb'})
df_a_5700_8gb = df_a_5700_8gb.rename(columns = {'y' : 'a_5700_8g'})
df_a_580_8gb = df_a_580_8gb.rename(columns = {'y' : 'a_580_8gb'})
df_a_radeon_VII_16gb = df_a_radeon_VII_16gb.rename(columns = {'y' : 'a_radeon_VII_16gb'})

"""Мерж датафреймов"""

df = df_n_3070_8gb.merge(df_n_2070_8gb, how='left', left_on=df_n_3070_8gb.index, right_on=df_n_2070_8gb.index)
df = df.merge(df_a_5700_8gb, how='left', left_on='key_0', right_on=df_a_5700_8gb.index)
df = df.merge(df_a_580_8gb, how='left', left_on='key_0', right_on=df_a_580_8gb.index)
df = df.merge(df_a_radeon_VII_16gb, how='left', left_on='key_0', right_on=df_a_radeon_VII_16gb.index)
df = df.rename(columns = {'key_0': 'date'})

df.index = df['date']
df.drop(['date'],axis=1, inplace=True)

df

df.index = pd.to_datetime(df.index)

plt.figure(figsize=(20,15))
plt.title("Средняя цена видеокарт")
plt.xlabel("Дата")
plt.ylabel("Цена, $")
plt.plot(df)

fig, ax = plt.subplots(figsize=(20, 10))

sns.heatmap(df.corr(), annot=True)

btc_usd = pd.read_csv('/content/BTC-USD (1).csv', index_col='Date')
eth_usd = pd.read_csv('/content/ETH-USD.csv', index_col='Date')

btc_usd

btc_usd.index = pd.to_datetime(btc_usd.index)
eth_usd.index = pd.to_datetime(eth_usd.index)
df['BTC'] = btc_usd['Adj Close']
df['ETH'] = eth_usd['Adj Close']

fig, ax = plt.subplots(figsize=(20, 10))


sns.heatmap(df.corr(), annot=True)

fig, ax = plt.subplots(figsize=(17, 12))
ax1 = ax.twinx()
ax.plot(df['a_5700_8g'],color='r', label='AMD Radeon RX 5700 8GB')
ax1.plot(df['BTC'],color='b', label='BTC')
ax.set_ylabel('Цена видеокарты, $')
ax1.set_ylabel('Цена BTC, $')

fig.legend(fontsize = 15,
          ncol = 1,    #  количество столбцов
          facecolor = 'oldlace',    #  цвет области
          edgecolor = 'r',    #  цвет крайней линии
          title = 'Цена',    #  заголовок
          title_fontsize = '20'    #  размер шрифта заголовка
         )