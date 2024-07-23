from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class HomeView(View):

    def get(self, request):
        return render(request, "home/home.html")


class OurTeamView(View):

    def get(self, request):
        return render(request, "home/our_team.html")
