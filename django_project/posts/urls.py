from django.urls import path
from . import views
from posts import views

urlpatterns = [
    path("", views.home),
    path("<name>", views.hello_there, name="hello_there"),
]