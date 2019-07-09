from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
	author=models.ForeignKey(User, on_delete=models.CASCADE)
	title=models.CharField(max_length=200)
	body=models.TextField()
	datetime=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def comments(self):
		return Comments.object.all(answer_post=self)

	class Meta:
		ordering = ['-datetime']


class Comment(models.Model):
	author=models.ForeignKey(User, on_delete=models.CASCADE)
	body=models.TextField()
	answer_post=models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, related_name="upost")
	answer_comment=models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="ucomment")
	datetime=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.body[:16]

	def comments(self):
		return Comment.object.all(answer_comment=self)

	class Meta:
		ordering = ['datetime']