from django.urls import path

from dynamic import views

urlpatterns = [
    path('', views.home, name="home")
]
