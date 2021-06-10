from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('register',views.registeruser,name='register'),

    path('login/',views.login,name='login'),
    path('signup', views.signup, name='signup'),
    path('contact/',views.contact,name='contact'),
    path('about/', views.about, name='about'),
    path('games/', views.games, name='games'),
    path('news/', views.news, name='news'),
    path('logout/', views.logout, name='logout'),
    path('payment1/',views.Paymentpage,name="payment1"),
    path('graphs/',views.graphs,name="graphs"),
    path('profile/', views.Profilepage, name="profile"),
    path('Account/', views.Account, name='Account'),


    ]