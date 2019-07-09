from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm
# Create your views here.

def posts_list(request):
	posts = Post.objects.all()
	form = PostForm()
	return render(request, 'blog/base.html', {'posts': posts, 'form':form})

def new_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			new_post = form.save(commit=False)
			new_post.author = request.user
			new_post.save()
			return redirect('posts_list')
		return redirect('post_list', {'error': 'невдача'})
