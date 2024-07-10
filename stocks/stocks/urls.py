from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path to admin page
    path('admin/', admin.site.urls),
    #path that connects to quotes.urls
    path('', include('quotes.urls')),
]
