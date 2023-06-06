from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.views.generic import View, TemplateView
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class HomePageView(TemplateView):
    template_name = 'users/home_page.html'
    extra_context = {'title': 'Home Page'}


class UserProfilePageView(LoginRequiredMixin, UserPassesTestMixin, View):
    model = get_user_model()

    def get(self, request, *args, **kwargs):
        return render(
            request=request,
            template_name="users/user_profile.html", 
            context={
                'title': 'User profile',
                'form': CustomUserForm(instance=self.model.objects.get(pk=self.kwargs['pk']))
            })
    

    def post(self, request, *args, **kwargs):
        form = CustomUserForm(request.POST, request.FILES, instance=self.model.objects.get(pk=self.kwargs['pk']))
        if form.is_valid():
            form.save()
            return redirect(reverse('home_page'))
        else:
            render(
                request=request,
                template_name="users/user_profile.html", 
                context={
                    'title': 'User profile',
                    'form': form
                })


    def test_func(self, *args, **kwargs):
        try:
            edit_user = self.model.objects.get(pk=self.kwargs['pk'])
        except self.model.DoesNotExist:
            return False
        user = self.request.user
        return edit_user == user