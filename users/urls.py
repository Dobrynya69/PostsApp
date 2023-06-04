from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name="home_page"),
    path('account/', include('allauth.urls')),
]
