#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    
    import pandas as pd
    import matplotlib.pyplot as plt
    # Для загрузки данных используем библиотеку yfinance
    import yfinance as yf
    
    #  Легенда
    GAZP = 'Газпром'
    ROSN = 'Росснефть'
    ADBE = 'Adobe'
    YNDX = 'Яндекс'
    ADS = 'Adidas'
    BABA = 'Alibaba'
    MOEX = 'Московская Биржа'
    SPBE = 'СПБ Биржа'
    
    tickers_list = [ 'GAZP.ME', 'ROSN.ME' ]    
    tickers_dict = {1:'ADBE', 2:'YNDX.ME'}
    tickers_tuple = ('ADS.DE', 'BABA')
    tickers_num = {'MOEX.ME', 'SPBE.ME'}  
    
    energy = "Сравнение акций Российских компаний энергетического сектора \
        с 1.01.2020 по 29.11.2022"
    it = "Сравнение трендов акций ИТ-компаний \
        с 1.01.2010 по 29.11.2022"
    consumer = "Сравнение акций компаний потребительского сектора \
        с 1.01.2015 по 29.11.2022"
    economic = "Сравнение акций компаний экономического сектора \
        с 1.01.2013 по 29.11.2022"
                
    def draw_plot(k1, k2, titul):
        plt.legend([k1, k2], title='легенда')
        plt.title(titul, fontsize=10)
        plt.ylabel('цена (x*100)', fontsize=8)
        plt.xlabel('год', fontsize=8)
        plt.grid(
            which="major", 
            color='k', 
            linestyle='-.', 
            linewidth=0.5)
        plt.show()
        return
    
    def download_data(d1,d2, tick:bool):   
        if tick == True:
            data = pd.DataFrame(columns=tickers_dict)  
            for ticker3 in tickers_dict:
                data[ticker3] = yf.download(tickers_dict[ticker3], d1, d2)['Adj Close']
        else:
            data = pd.DataFrame(columns=tickers_list)
            for ticker in tickers_list:
                data[ticker] = yf.download(ticker, d1, d2)['Adj Close']
        ((data.pct_change()+1).cumprod()).plot(figsize=(8, 5))
        return
    
    # Применение Списка
    download_data('2020-01-01', '2022-11-29', False)
    draw_plot(GAZP, ROSN, energy)

    # Применение Словаря
    download_data('2010-01-01', '2022-11-29', True)
    draw_plot(ADBE, YNDX, it)

    # Применение Кортежа
    download_data('2012-01-01', '2022-11-29', False)
    draw_plot(ADS, BABA, consumer)

    # Применение Множества
    download_data('2015-01-01', '2022-11-29', False)
    draw_plot(MOEX, SPBE, economic)
    