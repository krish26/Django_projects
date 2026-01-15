from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/',views.about, name='blog-about'),
    path('regiser/',user_views.register, name='user-register'),
    path('login/',user_views.login, name='user-login'),



]