from django.urls import path

from . import views

urlpatterns = [
    path("", views.kiosk_home, name="kiosk_home"),
    path("alumni/", views.kiosk_alumni, name="kiosk_alumni"),
    path("history/", views.kiosk_history, name="kiosk_history"),
]