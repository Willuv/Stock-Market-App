from django.shortcuts import render

#broswer request for home page
def home(request):
    return render(request, 'home.html', {})

#browser request for about page
def about(request):
    return render(request, 'about.html', {})