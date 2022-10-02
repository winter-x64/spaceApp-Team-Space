from django.urls import path
from editorApp import views

urlpatterns =[
    path('edit', views.editor)
]