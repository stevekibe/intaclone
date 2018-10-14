from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.all_post,name='post'),
    url(r'^new/post$',views.new_post, name='new-post'),
    url(r'^likes/$', views.like_post, name='like-post'),
    url(r'^user/(\d+)$',views.detail, name='detail'),
    url(r'^detail/edit/$', views.edit_detail, name='edit-detail'),
    url(r'^search/$', views.search_results, name='search-user'),
    url(r'^comment/(?P<image_id>\d+)', views.add_comment, name='comment'),
    url(r'^like/(?P<image_id>\d+)', views.like, name='like'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
