from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Count

from subreddits.models import Subreddit
from posts.models import Post

@login_required
def homepage(request):
    popular_subreddits = Subreddit.objects.annotate(total_members=Count('members')).order_by('-total_members')
    context = {'posts': Post.objects.filter(is_comment=False), 'popular_subreddits': popular_subreddits}
    return render(request, 'homepage.html', context)


def user_detail_view(request, id):
    user = get_user_model().objects.get(id=id)
    subreddits = Subreddit.objects.filter(members=user)
    posts = Post.objects.filter(author=user, is_comment=False)
    comments = Post.objects.filter(author=user, is_comment=True)
    context = {'user': user, 'subreddits': subreddits, 'posts': posts, 'comments': comments}
    return render(request, 'user_detail_view.html', context)
