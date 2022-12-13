from ticers import Ticers
from statsmodels.tsa.stattools import adfuller
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
# принудительно отключим предупреждения системы
import warnings
warnings.simplefilter(action = 'ignore', category = Warning)
from statsmodels.tsa.statespace.sarimax import SARIMAX

if __name__ == "__main__": 
    
    t = Ticers()
    t.dowload_data('GAZP', '2020-01-01', '2022-12-13')
    p = pd.read_csv('./data/company/GAZP.csv')

    # Индексируем поле Data
    p.set_index('Date', inplace=True)

    # Переводим текстоый формат в datetime для удобного проведения срезов
    p.index = pd.to_datetime(p.index)

    train = p[:'2022-01-01']
    test = p['2022-01-02':]

    # создадим объект этой модели
    model = SARIMAX(train, 
                    order = (1, 1, 1), 
                    seasonal_order = (0, 0, 0, 0)) # Без сезрнности и внешних данных - ARIMA
    
    # применим метод fit
    result = model.fit()
    
    # тестовый прогнозный период начнется с конца обучающего периода
    start = len(train)
    
    # и закончится в конце тестового
    end = len(train) + len(test) - 1
    b = 18500
    # применим метод predict
    predictions = result.predict()
    # pred.shift(1, axis=0)

    plt.plot(train, 'black')
    plt.plot(test, 'r')
    plt.plot(predictions, 'g--')

    # заголовок и подписи к осям
    plt.title("Обучающая выборка, тестовая выборка и тестовый прогноз")
    plt.ylabel('Стоимость')
    plt.xlabel('Дата')

    # добавим сетку
    plt.grid()
    plt.show()