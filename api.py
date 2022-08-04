import requests

def api_function():
    
    function = 'CURRENCY_EXCHANGE_RATE'
    from_symbol = 'USD'
    to_symbol = 'SGD'
    api_key = 'PRIKISIIKARLHL8Z'

    url= f'https://www.alphavantage.co/query?function={function}&from_currency={from_symbol}&to_currency={to_symbol}&apikey={api_key}'

    data = requests.get(url).json()

    return float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])

print(api_function())