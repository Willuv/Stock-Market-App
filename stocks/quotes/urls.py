from django.urls import path
from . import views

urlpatterns = [
    #path to home page
    path('', views.home, name="home"),
    #path to about page
    path('about.html', views.about, name="about"),

]