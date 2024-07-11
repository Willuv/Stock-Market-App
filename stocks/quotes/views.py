from django.shortcuts import render
from django.conf import settings

#broswer request for home page
def home(request):
    import requests
    import json

    #api_key taken from .env file
    api_key = settings.TIINGO_API_KEY
    url = f"https://api.tiingo.com/iex/?tickers=aapl&token={api_key}"
    api_request = requests.get(url)

    try:  
        # turn the api request into a dictionary and pull it out of the list its in
        api = api_request.json()[0]

    except Exception as e:
        api = "Error..."
    return render(request, 'home.html', {'api': api})

#browser request for about page
def about(request):
    return render(request, 'about.html', {})
