from django.shortcuts import render

#broswer request for home page
def home(request):
    return render(request, 'home.html', {})