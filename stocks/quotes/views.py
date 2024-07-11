from django.shortcuts import render

#Intrinio, 2 week free then must pay...
#d537a92d9a301f16e1bf3070daf481bb

#Alpha Vantage API (Potentially use)
#SYITEWAX5PIPY5ZO

#Polygon.io (prob use this one)
#UjyFDQigBbrjV_NfEPRc9kDC3SlqEsxR

#finazon
#7abf30fc13de4a8c98e2d3c201b43289yp

#tiingo
#53125623df24601520fe3ccf70180b07efd62258

#broswer request for home page
def home(request):
    import requests
    import json

    api_requests = requests.get("https://api.tiingo.com/iex/?tickers=aapl,&token=53125623df24601520fe3ccf70180b07efd62258")
    apiKey = '53125623df24601520fe3ccf70180b07efd62258'

    try:
        api_requests.raise_for_status()
        api = api_requests.json()
    except Exception as e:
        api = "Error..."
    return render(request, 'home.html', {'api': api})

#browser request for about page
def about(request):
    return render(request, 'about.html', {})