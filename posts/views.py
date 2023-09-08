from typing import Optional
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import *
from .forms import *

class PostsListPageView(View):
    model_name = Post
    form_name = SortForm
    template_name = 'posts/posts_list.html'

    def get(self, *args, **kwargs):
        data = self.model_name.objects.all()
        return render(
            template_name=self.template_name,
            request=self.request,
            context=
                {
                    'title': 'Post List',
                    'list': data,
                    'form': self.form_name()
                })
    

    def post(self, *args, **kwargs):
        filters = {
            'search': self.request.POST.get('search', None),
            'theme': self.request.POST.get('theme', None)
        }
        data = self.model_name.objects.all()
        for filter_key in filters:
            if filters[filter_key] != None and filters[filter_key] != '':
                match filter_key:
                    case 'search':
                        data = data.filter(title__icontains=filters[filter_key])
                    case 'theme':
                        data = data.filter(themes=filters[filter_key])
        return render(
            template_name=self.template_name,
            request=self.request,
            context=
                {
                    'title': 'Post List',
                    'list': data,
                    'form': self.form_name(self.request.POST)
                })


class UserPostsListPageView(LoginRequiredMixin, UserPassesTestMixin, View):
    model_name = Post
    form_name = SortForm
    template_name = 'posts/user_posts_list.html'


    def test_func(self):
        try:
            right_user = get_user_model().objects.get(pk = self.kwargs['pk'])
        except get_user_model().DoesNotExist:
            return False
        
        current_user = self.request.user
        return right_user == current_user


    def get(self, *args, **kwargs):
        data = self.model_name.objects.filter(author=self.request.user)
        return render(
            template_name=self.template_name,
            request=self.request,
            context=
                {
                    'title': 'Post List',
                    'list': data,
                    'form': self.form_name()
                })
    

    def post(self, *args, **kwargs):
        filters = {
            'search': self.request.POST.get('search', None),
            'theme': self.request.POST.get('theme', None)
        }
        data = self.model_name.objects.filter(author=self.request.user)
        for filter_key in filters:
            if filters[filter_key] != None and filters[filter_key] != '':
                match filter_key:
                    case 'search':
                        data = data.filter(title__icontains=filters[filter_key])
                    case 'theme':
                        data = data.filter(themes=filters[filter_key])
        return render(
            template_name=self.template_name,
            request=self.request,
            context=
                {
                    'title': 'Post List',
                    'list': data,
                    'form': self.form_name(self.request.POST)
                })


class PostDetailPageView(View):
    model_name = Post
    template_name = 'posts/post_detail.html'

    def get(self, *args, **kwargs):
        post = self.model_name.objects.get(pk=kwargs['pk'])
        return render(
            template_name=self.template_name,
            request=self.request,
            context=
                {
                    'title': post.title,
                    'post': post
                })
    

class PostCreatePageView(LoginRequiredMixin, View):
    model_name = Post
    theme_model_name = Theme
    form_name = PostForm
    template_name = 'posts/post_create.html'


    def get(self, *args, **kwargs):
        return render(
            template_name=self.template_name,
            request=self.request,
            context=
                {
                    'title': "Create a post",
                    'form': self.form_name()
                })


    def post(self, *args, **kwargs):
        form = self.form_name(self.request.POST, self.request.FILES)
        if form.is_valid():
            record = self.model_name.objects.create(
                author = self.request.user,
                title = self.request.POST.get('title', ''),
                body = self.request.POST.get('body', ''),
                image = self.request.FILES.get('image'),
            )
            for theme in self.request.POST.getlist('themes'):
                record.themes.add(self.theme_model_name.objects.get(pk=theme))
            return redirect(reverse('post_detail', kwargs={'pk': record.pk}))
        else:
            return render( 
                template_name=self.template_name,
                request=self.request,
                context=
                    {
                        'title': "Create a post",
                        'form': form
                    })
        

class PostChangePageView(LoginRequiredMixin, UserPassesTestMixin, View):
    model_name = Post
    theme_model_name = Theme
    form_name = PostForm
    template_name = 'posts/post_change.html'

    def test_func(self):
        try:
            right_user = get_user_model().objects.get(pk = self.kwargs['user_pk'])
        except get_user_model().DoesNotExist:
            return False
        
        current_user = self.request.user
        return right_user == current_user


    def get(self, *args, **kwargs):
        post = self.model_name.objects.get(pk = self.kwargs['post_pk'])
        return render(
            template_name=self.template_name,
            request=self.request,
            context=
                {
                    'title': "Change a post",
                    'form': self.form_name(instance=post)
                })


    def post(self, *args, **kwargs):
        post = self.model_name.objects.get(pk = self.kwargs['post_pk'])
        form = self.form_name(self.request.POST, self.request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse('post_detail', kwargs={'pk': post.pk}))
        else:
            return render( 
                template_name=self.template_name,
                request=self.request,
                context=
                    {
                        'title': "Change a post",
                        'form': form
                    })