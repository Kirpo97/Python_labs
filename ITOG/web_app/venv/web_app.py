from flask import Flask
from flask import render_template
from ticers import Ticers
import pandas as pd

app = Flask(__name__)
t = Ticers()

@app.route("/")
def chart():
    t = Ticers().dowload_data('GAZP', '2020-01-01', '2022-12-13')
    p = pd.read_csv('./data/company/GAZP.csv')    
    legend = 'Monthly Data'
    labels = p['Date']
    values = p['GAZP']
    return render_template('index.html', values=values, labels=labels, legend=legend)

if __name__ == "__main__": 

    app.run('127.0.0.1', port=5001 ,debug=True)
