from django.urls import path

from . import views

urlpatterns = [
    path("", views.kiosk_home, name="kiosk_home"),
    path("alumni/", views.kiosk_alumni, name="kiosk_alumni"),
    path("alumni/<slug:slug>/", views.kiosk_alumni_detail, name="kiosk_alumni_detail"),
    path("history/", views.kiosk_history, name="kiosk_history"),
    path("history/<slug:slug>/", views.kiosk_history_detail, name="kiosk_history_detail"),
    path("archives/", views.kiosk_archives, name="kiosk_archives"),
]