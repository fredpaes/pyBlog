from django.shortcuts import render
from app_one.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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

'''def post_list(request):
    subs = Post.objects.filter(
        status = 'published'
    )
    return render(request, 'post/post_list.html',
                  {'subidos': subs})'''

def post_list(request):
    object_list = Post.objects.filter(
        status = 'published'
    )
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        subs = paginator.page(page)
    except PageNotAnInteger:
        subs = paginator.page(1)
    except EmptyPage:
        subs = paginator.page(paginator.num_pages)

    return render(request, 'post/post_list.html',
                  {'subidos': subs})