#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    # Импортируем matplotlib для вывода графика
    import matplotlib.pyplot as plt

    # Импортируем yfinance для загрузки данных об изменениях акций через Yahoo-поисковик
    import yfinance as yf
    
    # Загружаем график Газпрома с 2016-01-01 по 2022-08-01
    data = yf.download('GAZP.ME',
                       '2016-01-01', 
                       '2022-08-01')['Adj Close'].plot(figsize=(10, 8))

    # Формируем и выводим график
    plt.legend(['Газпром'], title='Легенда')
    plt.title("График изменения акций", fontsize=16)
    plt.ylabel('Цена', fontsize=14)
    plt.xlabel('Год', fontsize=14)
    plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
    plt.show()
    