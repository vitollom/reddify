from django.shortcuts import render, HttpResponseRedirect, redirect, reverse
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from posts.models import Post
from subreddits.models import Subreddit
from posts.forms import CreatePostForm, CreateCommentForm

# Create your views here.
def post_view(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post.html', { 'post': post })

@login_required
def create_post_view(request, id):
  subreddit = Subreddit.objects.get(id=id)

  if request.method == 'POST':
    form = CreatePostForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      post = Post(
        title = data.get('title'),
        body = data.get('body'),
        is_comment = False,
        author = request.user,
        subreddit = subreddit,
      )
      post.save()
      subreddit.posts.add(post)
      return HttpResponseRedirect(reverse('post', args=(post.id,)))

  form = CreatePostForm()

  return render(request, 'create_post.html', { 'form': form })

@login_required
def create_comment_view(request, id):
  post = Post.objects.get(id=id)

  if request.method == 'POST':
    form = CreateCommentForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      comment = Post(
        body = data.get('body'),
        is_comment = True,
        author = request.user,
        parent = post
      )
      comment.save()
      return HttpResponseRedirect(reverse('post', args=(post.id,)))

  form = CreateCommentForm()

  return render(request, 'create_post.html', { 'form': form })


def upvote_post(request, id):
  post = Post.objects.get(id=id)
  if request.user in post.up_votes.all():
    post.up_votes.remove(request.user)
  elif request.user in post.down_votes.all():
    post.down_votes.remove(request.user)
    post.up_votes.add(request.user)
  else:
    post.up_votes.add(request.user)
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def downvote_post(request, id):
  post = Post.objects.get(id=id)
  if request.user in post.down_votes.all():
    post.down_votes.remove(request.user)
  elif request.user in post.up_votes.all():
    post.up_votes.remove(request.user)
    post.down_votes.add(request.user)
  else:
    post.down_votes.add(request.user)
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))