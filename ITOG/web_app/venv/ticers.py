import pandas as pd
import yfinance as yf 

class Ticers(): 
    def __init__(self):
        self.GAZP = 'GAZP.ME'
            
    def __call__(self):
        return self.__dict__
     
    def dowload_data(self, company, data1, data2):
        tickers_dict = Ticers().__dict__
        data = pd.DataFrame(columns=tickers_dict)  
        data[company] = yf.download(tickers_dict[company], data1, data2)['Adj Close']
        data.to_csv('./data/company/' + company + '.csv')
   