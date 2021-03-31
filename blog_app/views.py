from django.shortcuts import render
from django.views.generic import (TemplateView,DeleteView, ListView, DetailView, CreateView, UpdateView)
from blog_app.models import Post, Comment
# if we use class based view then we use this library for login required method
from django.contrib.auth.mixins import LoginRequiredMixin
# if we use funciton base view then we use this library for login required method
from django.contrib.auth.decorators import login_required
from blog_app.forms import PostFrom, CommentForm
from django.urls import reverse_lazy
# Create your views here.

class Aboutview(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail.html'
    form_class = PostFrom
    model =  Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail.html'
    form_class = PostFrom
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')
