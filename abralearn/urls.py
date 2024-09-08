"""
URL configuration for abralearn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from allauth.account.views import ConfirmEmailView
from core.views import CourseListView

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('api/auth/', include('dj_rest_auth.urls')),  # Login, Logout, Password Reset
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # User Registration
    path(
        'api/auth/registration/account-confirm-email/<key>/',
        ConfirmEmailView.as_view(),
        name='account_confirm_email',
    ),
    path('api/courses/', CourseListView.as_view(), name='course-list'),  # Update to 'api/courses/'
]
