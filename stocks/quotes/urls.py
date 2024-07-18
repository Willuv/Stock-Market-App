from django.urls import path
from . import views

urlpatterns = [
    #path to home page
    path('', views.home, name="home"),
    #path to about page
    path('about.html', views.about, name="about"),
    #path to add_stock
    path('add_stock.html', views.add_stock, name="add_stock"),
    #path for delete function
    path('delete/<stock_id>', views.delete, name="delete"),
    #path to delete_stock
    path('delete_stock.html', views.delete_stock, name="delete_stock"),
]