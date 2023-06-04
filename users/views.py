from django.shortcuts import render
from django.views.generic import View

class HomePageView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request=request,
            template_name='users/home_page.html',
            context={'title': 'Home Page'})