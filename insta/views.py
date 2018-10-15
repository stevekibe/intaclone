from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.contrib.auth.models import User
from .models import Image,Detail,Comment,Likes
from .forms import NewPostForm, SignupForm,DetailForm,CommentsForm
from friendship.models import Friend, Follow, Block

@login_required(login_url='/accounts/login/')
def all_post(request):
    images = Image.get_images().order_by('-pub_date')
    details = User.objects.all()
    people = Follow.objects.following(request.user)
    comments = Comment.objects.all()
    likes = Likes.objects.all()

    return render (request, "insta-posts/index.html", {"images":images,"details":details,"people":people, "comments":comments,"likes":likes})

def search_results(request):

    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_detail = User.objects.filter(username__icontains=search_term)
        message = f"{search_term}"
        details = User.objects.all()
        people = Follow.objects.following(request.user)
        print(details)

        return render(request, 'insta-posts/search.html',{"message":message,"posts":searched_posts})


@login_required(login_url='accounts/login')
def new_post(request):
    detail = Detail.objects.all()
    for detail in detail:
        if request.method == 'POST':
            form = NewPostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.detail = detail
                post.editor = current_user
                post.save()
            return redirect ('all_post')

        else:
            form = NewPostForm()
    return render(request, 'new_post.html', )

@login_required(login_url='/accounts/login/')
def like_post(request):
    image = get_object_or_404(Image, id=request.POST.get('image_id'))
    image.likes.add(request.user)
    return redirect('all_post')


@login_required(login_url='accounts/login')
def detail(request, user_id):
    title = "Profile"
    images = Image.get_image_by_id(id= user_id).order_by('pub_date')
    details = User.objects.get(id=user_id)
    users = User.objects.get(id=user_id)
    follow = len(Follow.objects.followers(users))
    following = len(Follow.objects.following(users))
    people = Follow.objects.following(request.user)

    return render(request, 'detail/detail.html',{'title':title,"images":images,"follow":follow, "following":following,"details":details,"people":people})

@login_required(login_url='accounts/login/')
def edit_detail(request):
    current_user = request.user
    detail = Detail.objects.get(user= request.user)
    if request.method == 'POST':
        form = DetailForm(request.POST, request.FILES)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.save()
        return redirect('all_post')
    else:
        form = DetailForm()
    return render(request, 'detail/edit-detail.html', {"form": form,})

@login_required(login_url='/accounts/login/')
def add_comment(request, image_id):
    images = get_object_or_404(Image, pk=image_id)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.image = images
            comment.save()
    return redirect('all_post')

def like(request, image_id):
   current_user = request.user
   liked_post = Image.objects.get(id=image_id)
   new_like, created = Likes.objects.get_or_create(user_like=current_user, liked_post=liked_post)
   new_like.save()

   return redirect('all_post')

@login_required(login_url='/accounts/login/')
def follow(request,user_id):
    other_user = User.objects.get(id = user_id)
    follow = Follow.objects.add_follower(request.user, other_user)

    return redirect('all_post')

@login_required(login_url='/accounts/login/')
def unfollow(request,user_id):
    other_user = User.objects.get(id = user_id)

    follow = Follow.objects.remove_follower(request.user, other_user)

    return redirect('all_post')