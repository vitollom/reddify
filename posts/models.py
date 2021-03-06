from mptt.models import MPTTModel, TreeForeignKey
from django.db import models
from django.utils import timezone


class Post(MPTTModel):
	title = models.CharField(max_length=100, null=True, blank=True)
	body = models.TextField(null=True, blank=True)
	is_comment = models.BooleanField(default=False)
	author = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='user')
	up_votes = models.ManyToManyField('users.User', symmetrical=False, blank=True, related_name='post_up_votes')
	down_votes = models.ManyToManyField('users.User', symmetrical=False, blank=True, related_name='post_down_votes')
	subreddit = models.ForeignKey('subreddits.Subreddit', on_delete=models.CASCADE, null=True, blank=True)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
	created_at = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title or self.body
