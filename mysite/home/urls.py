from django.urls import path
from home.views import HomeView, OurTeamView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),  # Головна сторінка
    path("our_team", OurTeamView.as_view(), name="our_team"),
]
