from django.urls import path
from . import views

urlpatterns = [
    path('account', views.account, name='account'),
    
    path('home/', views.home, name='home'),

    path('newpost/', views.newpost, name='newpost'),

    path('newsfeed/', views.newsfeed, name='newsfeed'),

    path('postdetails/', views.postdetails, name='postdetails'),

    path('profile/', views.profile, name='profile'),

    path('search/', views.search, name='search'),

    path('settings/', views.settings, name='settings'),

    path('', views.signin, name='signin'),

    path('signup/', views.signup, name='signup')
]

