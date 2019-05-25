"""aqumenv2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.urls import include
from users import views as users_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("study.urls")),
    path('join/', users_views.join, name="join"),
    # path('login/', users_views.login_view, name="login"),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', users_views.ProfileInfoCBV.as_view(), name="profile"),
    # path('profile/', users_views.profile, name='profile'),
    # path('', users_views.home_page_view, name="home_page_view"),
]




# What is this for?
if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # from corey schafer but raises Empty static prefix not permitted
    urlpatterns += static(settings.STATIC_URL , document_root=settings.STATIC_ROOT) # fix apparenly from Django doc
