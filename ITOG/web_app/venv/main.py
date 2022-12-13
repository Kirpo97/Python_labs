from pandas import read_csv, DataFrame
import statsmodels.api as sm
from statsmodels.iolib.table import SimpleTable
from sklearn.metrics import r2_score
import ml_metrics as metrics

import matplotlib.pyplot as plt
# Для загрузки данных используем библиотеку yfinance
import yfinance as yf

data = DataFrame.DataFrame()  
data[0] = yf.download('GAZP.ME', '2020-01-01', '2022-11-29')['Adj Close']
    
#dataset = read_csv('tovar_moving.csv',';', index_col=['date_oper'], parse_dates=['date_oper'], dayfirst=True)
#dataset.head()
data.head()