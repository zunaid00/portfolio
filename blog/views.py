from django.shortcuts import render,get_object_or_404
from . models import blog
# Create your views here.
def allblogs(request):
    blogs=blog.objects.all()
    return render(request,'blog/allblogs.html',{'blogs':blogs})

def detail(request,blog_id):
    blogdetail =blog.objects.get(id=blog_id)
    return render(request,'blog/detail.html',{'blogdetail':blogdetail})

