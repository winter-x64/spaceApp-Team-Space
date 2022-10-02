from django.urls import path
from editorApp import views

urlpatterns =[
    # Editor URL
    path('edit', views.editor),

    # Preview URL
    path('preview', views.preview),

    # uploads page URL
    path('upload', views.upload),

    # DownLoads
    path('downloads', views.download),
    ]