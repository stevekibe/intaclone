from django.shortcuts import render
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Profile

def all_post(request):
    post = Profile.objects.all()

    return render (request, "insta-posts/index.html", {"post":post})