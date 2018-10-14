from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.all_post,name='post'),
    url(r'^new/post$',views.new_post, name='new-post')
    url(r'^likes/$', view.like_post, name='like')
    url()

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
