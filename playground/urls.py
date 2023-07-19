from django.urls import path
from . import views

# map URLs in this file

# URl Config
urlpatterns = [
    path('alive/', views.alive), # in main folder/urls.py we have specified "playground" path by default
    path('tagh1/', views.tagh1) 
]