from flask import Flask, render_template, request
import requests

from conv import convert

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/results', methods=['GET', 'POST'])
def currency():
  info = []  # Declare info variables with a default value
  bugger = 0
    
  if request.method == 'POST':
    amount = float(request.form['amount'])
    start = request.form['from_currency']
    end = request.form['to_currency']
    total = convert(amount, start.lower(), end)
    if end == "JPY":
            end = "JPN"
    elif end =="GBP":
      end = "GBR"  
    response = requests.get(f'https://data.nasdaq.com/api/v3/datasets/ECONOMIST/BIGMAC_{end}?api_key=-2wrhELmEngGvs1ysFjB')
    data = response.json()
    column_names = data['dataset']['column_names']
    dollar_price_index = column_names.index('local_price')
    dollar_price_value = data['dataset']['data'][0][dollar_price_index]
        
    info = [amount, start, end, total]
    bugger = round(info[3] / dollar_price_value)
    return render_template("result.html", info=info, bugger=bugger)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
