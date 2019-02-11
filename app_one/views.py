from django.shortcuts import render
from app_one.models import Post

# Create your views here.
def home(request):
    return render(request, 'post/index.html',
                  {'posts': Post.objects.count(),
                  'dfg': 'Django'})

def post_list(request):
    # subs = Post._meta.model.objects.all()
    # subs = Post.objects.all()
    subs = Post.objects.filter(
        status = 'published'
    )
    return render(request, 'post/index.html',
                  {'subidos': subs})

def post_list(request):
    subs = Post.objects.filter(
        status = 'draft'
    )
    return render(request, 'post/post_list.html',
                  {'subidos': subs})