from django.urls import path
from editorApp import views

urlpatterns =[
    path('edit', views.editor),
    path('preview', views.preview),
    path('upload', views.upload),
    path('downloads', views.download),
    ]