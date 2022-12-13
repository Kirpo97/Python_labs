from flask import Flask
from flask import render_template
from ticers import Ticers
    
app = Flask(__name__)
t = Ticers()

@app.route("/")
def chart():
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = t.dowload_data('2022-01-01', '2022-11-29')
    return render_template('index.html', values=values, labels=labels, legend=legend)

if __name__ == "__main__": 
    app.run('127.0.0.1', port=5001 ,debug=True)
