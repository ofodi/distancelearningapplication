"""distancelearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

import project

urlpatterns = [
    path('', include('project.urls')),
    path('admin/', admin.site.urls),
    path('account/dashboard/', include('project.urls')),
    path('account/register', include('project.urls')),
    path('account/loginpage', include('project.urls')),
    path('account/profile', include('project.urls')),
    path('editprofile/<str:pk>', include('project.urls')),
    path('delete_profile/<str:pk>', include('project.urls')),
    path('account/course_details/<str:pk>', include('project.urls')),
    path('course_registration', include('project.urls'))
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)