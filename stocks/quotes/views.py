from django.shortcuts import render

#Intrinio, 2 week free then must pay...
#d537a92d9a301f16e1bf3070daf481bb

#Alpha Vantage API (Potentially use)
#SYITEWAX5PIPY5ZO

#Polygon.io (prob use this one)
#UjyFDQigBbrjV_NfEPRc9kDC3SlqEsxR

#broswer request for home page
def home(request):
    import requests
    import json

    api_requests = requests.get("https://api.polygon.io/v1/open-close/AAPL/2023-01-09?adjusted=true&apiKey=UjyFDQigBbrjV_NfEPRc9kDC3SlqEsxR")
    apiKey = 'UjyFDQigBbrjV_NfEPRc9kDC3SlqEsxR'

    try:
        api = json.loads(api_requests.content)
    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', {'api': api})

#browser request for about page
def about(request):
    return render(request, 'about.html', {})