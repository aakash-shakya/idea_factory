from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View,DetailView

from posts.models import Post
from comments.models import Comment
from comments.forms import CommentForm


class IndexView(View):
  def get(self, request, *args, **kwargs):
    post = Post.objects.all()
    return render(request, 'pages/home.html', {'post_list':post})

class DashboardView(LoginRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    return render(request, 'pages/dashboard.html', {})

class AboutView(View):
  def get(self, request, *args, **kwargs):
    return render(request, 'pages/about.html', {})

class PostDetailView(DetailView):
  queryset = Post.objects.all()
  context_object_name = 'post'
  lookup = 'id'
  
  def get_object(self, *args, **kwargs):
    return get_object_or_404(Post, pk=self.kwargs.get(self.lookup))
  
  def get_context_data(self, *args, **kwargs):
    context = super(PostDetailView, self).get_context_data(*args, **kwargs)
    context['title'] = 'Post Detail'
    return context