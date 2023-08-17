from django.urls import path
from . import views

# map URLs in this file

# URl Config
urlpatterns = [
    path('alive/', views.alive), # in main folder/urls.py we have specified "playground" path by default
    path('tagh1/<int:id>', views.tagh1),
    path('teams/', views.get_team),
    path('create/', views.createTeam)
]