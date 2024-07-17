from django.shortcuts import render
from django.conf import settings

#broswer request for home page
def home(request):
    import requests
    import json

    #if someone filled out the form
    if request.method == 'POST':
        ticker = request.POST['ticker']
        #api_key taken from .env file
        api_key = settings.TIINGO_API_KEY
        #url to the ticker information we want
        url = f"https://api.tiingo.com/iex/?tickers={ticker}&token={api_key}"
        #request the info
        api_request = requests.get(url)

        try:  
            # turn the api request into a dictionary and pull it out of the list its in
            api = api_request.json()[0]
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api': api})
    #else say to enter a ticker
    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})

#browser request for about page
def about(request):
    return render(request, 'about.html', {})


def add_stock(request):
        return render(request, 'add_stock.html', {})