from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import PostForm, CommentForm
from .models import Post, Comment

def post_home(request):
    return render(request, 'blog/post_home.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_cs(request):
    inposts = Post.objects.filter(tag__contains='Cs').order_by('published_date')
    posts = inposts.filter(published_date__lte = timezone.now())
    return render(request, 'blog/post_cs.html', {'posts':posts})

def post_art(request):
    inposts = Post.objects.filter(tag__contains='Ar').order_by('published_date')
    posts = inposts.filter(published_date__lte = timezone.now())
    return render(request, 'blog/post_art.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form' : form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk = pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = PostForm(instance = post)
    return render(request, 'blog/post_edit.html', {'form':form})

def contact(request):
    return render(request, 'blog/contact.html')

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk = pk)
    post.publish()
    return redirect('post_detail', pk = pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    tag = post.tag
    post.delete()
    if(tag == 'CS'):
        return redirect('post_cs')
    else:
        return redirect('post_art')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)