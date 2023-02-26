from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('setting/', views.setting, name='setting'),
    path('homepage/', views.homepage, name='homepage'),
]