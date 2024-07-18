from django.shortcuts import render, redirect
from django.conf import settings
from .models import Stock
from .forms import StockForm
from django.contrib import messages

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

#browser request for add_stock page
def add_stock(request):
    import requests
    import json
    # if someone filled the form and clicked the button
    if request.method == 'POST':
        # create a form variable with the ticker
        form = StockForm(request.POST or None)

        # check the form is valid
        if form.is_valid():
            # save to database
            form.save()
            # print success messgae
            messages.success(request, ("Stock Has Been Added!"))
            #return to add_stock page
            return redirect('add_stock')
    else:
        ticker = Stock.objects.all()
        # lists of all the tickers that are decoded from the json
        output = []
        for ticker_item in ticker:
            api_key = settings.TIINGO_API_KEY
            url = f"https://api.tiingo.com/iex/?tickers={ticker_item}&token={api_key}"
            #request the info
            api_request = requests.get(url)
            try:  
                # turn the api request into a dictionary and pull it out of the list its in
                api = api_request.json()[0]
                output.append(api)
            except Exception as e:
                api = "Error..."
            
        return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})

#function to delete stock from database
def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock Has Been Deleted!"))
    return redirect(delete_stock)


#browser request for delete_stock page
def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, 'delete_stock.html', {'ticker': ticker})