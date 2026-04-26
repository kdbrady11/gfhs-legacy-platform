from django.urls import path

from . import views

urlpatterns = [
    path("contribute/", views.contribute_materials, name="contribute_materials"),
    path("contribute/thanks/", views.contribution_thanks, name="contribution_thanks"),
]