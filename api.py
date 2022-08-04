import requests

def api_function():
    #this function is created to extract the currency exchange rate through the api.
  
    api_key = 'PRIKISIIKARLHL8Z'
    url= f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}'
    response = requests.get(url).json()
    
    #return float is used to specifically retrieve the Realtime Currency Exchange Rate and Exchange Rate.
    return float(response['Realtime Currency Exchange Rate']['5. Exchange Rate'])

print(api_function())