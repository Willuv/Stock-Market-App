from django.shortcuts import render

#Intrinio, 2 week free then must pay...
#d537a92d9a301f16e1bf3070daf481bb
#Alpha Vantage API (Potentially use)
#SYITEWAX5PIPY5ZO
#Polygon.io (prob use this one)
#UjyFDQigBbrjV_NfEPRc9kDC3SlqEsxR
#broswer request for home page
def home(request):
    return render(request, 'home.html', {})

#browser request for about page
def about(request):
    return render(request, 'about.html', {})