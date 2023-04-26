from flask import Flask, render_template, url_for, request, redirect
import requests

app = Flask(__name__)


@app.route('/')
@app.route('/cover')
def cover():
    return render_template('cover.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/pass-generator')
def pass_generator():
    return render_template('pass-generator.html')


@app.route('/calculator')
def calculator():
    return render_template('calculator.html')


@app.route('/exchange', methods=['POST', 'GET'])
def exchange():
    """Gets acces to exchangerate-api.com with API key, returns default page with 'GET' method,
        converts and displays calculated value with 'POST' method"""
    response = requests.get(
        url='https://v6.exchangerate-api.com/v6/5e3e41fad6586fa3aa5dcd3f/latest/USD').json()
    currencies = response.get('conversion_rates')
    last_update = response.get('time_last_update_utc')
    data = {'currencies': currencies, 'last_update': last_update}

    if request.method == 'GET':

        return render_template('exchange.html', data=data)

    if request.method == 'POST':
        amount = request.form.get('amount')
        from_currency = request.form.get('from')
        to_currency = request.form.get('to')
        result = round(
            (currencies[to_currency] / currencies[from_currency]) * float(amount), 4)
        data.setdefault('result', result)
        data.setdefault('amount', amount)
        data.setdefault('from_currency', from_currency)
        data.setdefault('to_currency', to_currency)

        return render_template('exchange.html', data=data)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/sign-up')
def sign_up():
    return render_template('sign_up.html')


if __name__ == '__main__':
    app.run(debug=True)
