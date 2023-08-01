from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('profile/<pk>/', UserProfilePageView.as_view(), name='user_profile'),
    path('accounts/', include('allauth.urls')),
    path('account/', include('allauth.urls')),

]
