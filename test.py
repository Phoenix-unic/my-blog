import requests


response = requests.get(
    url='https://v6.exchangerate-api.com/v6/5e3e41fad6586fa3aa5dcd3f/latest/USD').json()
rates = response.get('conversion_rates')
for rate in rates:
    print(rate)