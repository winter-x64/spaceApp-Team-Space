from django.urls import path
from mainApp import views

urlpatterns =[

    path('', views.landingPage),
    path('home', views.home),
    path('aboutUs', views.aboutPage)

]