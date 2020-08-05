from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Post, PostDetails
from .forms import NewCommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

# Not using this part of code
def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blogapp/home.html', context)

#Using class based views to render homepage
class PostListView(ListView):
	model = Post
	template_name = 'blogapp/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 10

class UserPostListView(ListView):
	model = Post
	template_name = 'blogapp/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

#Using class based views to render posts
class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'subhead', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def comments(request, pk):
	related_post = get_object_or_404(Post, pk=pk)
	return render(request, 'blogapp/comments.html', {'related_post':related_post})

@login_required
def newcomment(request,pk):
	related_post = get_object_or_404(Post, pk=pk)
	user = User.objects.first()
	if request.method == 'POST':
		form = NewCommentForm(request.POST)
		if form.is_valid():
			data = form.save(commit=False)
			data.post = related_post
			data.username = user
			data.save()
			return redirect('comments', pk=related_post.pk)
	else:
		form = NewCommentForm()
	return render(request, 'blogapp/new_comment.html',  {'related_post':related_post, 'form':form})

	
def about(request):
	return render(request, 'blogapp/about.html', {'title': 'About'})