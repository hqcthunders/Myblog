from django.urls import path
from . import views

urlpatterns = [
    path("", views.lists, name='blog'),
    path("<int:id>/", views.posts, name='post'),
]
