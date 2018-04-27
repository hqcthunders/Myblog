from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("pages/checkfile.html", views.check_file, name='check')
]
