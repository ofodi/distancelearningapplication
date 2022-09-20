from unicodedata import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),
    path('account/dashboard/', views.dashboard, name='account/dashboard'),
    path('account/register/', views.register, name='account/register'),
    path('account/loginpage/', views.loginpage, name='account/login'),
    path('account/logout/', views.logoutUser, name='logout'),
    path('profile/', views.createprofile, name='profile'),
    path('editprofile/<str:pk>/', views.editprofile, name='editprofile'),
    path('delete_profile/<str:pk>/', views.deleteProfile, name='delete_profile'),
    path('account/course_details/<str:pk>/', views.course_detail, name='account/course_details'),
    path('course_registration/', views.course_registration, name='course_registration'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard')
    # path('contact', views.contact, name='ContactUs')
    
    ]
