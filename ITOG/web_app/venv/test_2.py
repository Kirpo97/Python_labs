# Автокорреляция

from ticers import Ticers
import matplotlib.pyplot as plt

# импортируем автокорреляционную функцию (ACF)
from statsmodels.graphics.tsaplots import plot_acf

if __name__ == "__main__": 
    plot_acf(data, alpha = None)
    plt.show()
    t = Ticers()
    t.dowload_data('GAZP','2020-01-01', '2022-12-10')
    p = pd.read_csv('./data/company/GAZP.csv')
    
    # Индексируем поле Data
    p.set_index('Date', inplace=True)

    # Переводим текстоый формат в datetime для удобного проведения срезов
    p.index = pd.to_datetime(p.index)
    
    adf_test = adfuller(p['#P'])
    # выведем p-value
    print('p-value = ' + str(adf_test[1]))