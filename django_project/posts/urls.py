from django.urls import path, re_path
from . import views
from posts import views

urlpatterns = [
    path("home", views.home),
    re_path(r'', views.home),
    path("<name>", views.hello_there, name="hello_there"),
]