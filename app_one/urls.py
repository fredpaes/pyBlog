from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'home/', home),
    url(r'posts/', post_list),
    url(r'^post/new$', new_post, name="newpost"),
]