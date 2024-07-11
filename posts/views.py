from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Post, Comment

def post_list(request):
    posts=Post.objects.all()
    context={
        "posts":posts,
    }
    return render(request, 'post_list.html', context)

def post_create(request):
    if request.method=="POST":
        Post.objects.create(
            title=request.POST["title"],
            user=request.POST["user"],
            content=request.POST["content"]
        )
        return redirect("/posts")
    return render(request, 'post_create.html')

def post_detail(request, pk):
    post=Post.objects.get(id=pk)
    
    # 제일 작은 값과 제일 큰 값에 예외 처리 필요
    previous_id=Post.objects.filter(id__lt=pk).order_by("-id")[0].pk
    next_id=Post.objects.filter(id__gt=pk).order_by("id")[0].pk
    
    comments=Comment.objects.filter(post=pk)
    
    context={
        "post":post,
        "previous_post_id":previous_id,
        "next_post_id":next_id,
        "comments": comments,
    }
    return render(request, 'post_detail.html', context)

def post_update(request, pk):
    post=Post.objects.get(id=pk)
    if request.method=="POST":
        post.title=request.POST["title"]
        post.user=request.POST["user"]
        post.content=request.POST["content"]
        
        post.save()
        
        return redirect(f"/posts/{pk}")
        
    context={
        "post":post
    }
    return render(request, 'post_update.html', context)

def post_delete(request, pk):
    if request.method=="POST":
        post=Post.objects.get(id=pk)
        post.delete()
    return redirect("/posts")

def comment_create(request, pk):
    if request.method=="POST":
        post=Post.objects.get(id=pk)
        Comment.objects.create(
            post=post,
            content=request.POST["content"]
        )
    
    return redirect(f"/posts/{pk}")