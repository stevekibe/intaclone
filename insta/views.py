from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
import datetime as dt
from .models import Profile,Detail,Comment
from .forms import NewPostForm

def all_post(request):
    post = Profile.objects.all()

    return render (request, "insta-posts/index.html", {"post":post})

def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        message = f"{search_term}"

        return render(request, 'insta-posts/search.html',{"message":message,"posts":searched_posts})


@login_required(login_url='accounts/login')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.editor = current_user
            post.save()
        return redirect ('all_post')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html',{"form":form})

@login_required(login_url='accounts/login')
def detail(request, user_id):
    title = "Profile"
    images = Image.get_image_by_id(id= user_id).order_by('-posted_on')
    details = User.objects.get(id=user_id)
    users = User.objects.get(id=user_id)
    follow = len(Follow.objects.followers(users)))
    following = len(Follow.objects.following(users))
    people = Follow.objects.following(request.user)

    return render(request, 'detail/detail.html',{'title':title,"images":images,"follow":follow, "following":following,"profiles":profiles,"people":people})

@