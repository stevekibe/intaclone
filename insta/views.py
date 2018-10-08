from django.shortcuts import render
from django.http  import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
import datetime as dt
from .models import Profile
from .forms import NewPostForm

def all_post(request):
    post = Profile.objects.all()

    return render (request, "insta-posts/index.html", {"post":post})

def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Profile.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'insta-posts/search.html',{"message":message,"posts":searched_posts})


@login_required(login_url='accounts/login')
def new_post(request):
    current_user = request.current_user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return redirect ('all_post')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html',{"form":form})