"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth import views as auth_views

from poll.views import PostDeleteView, PostCreateView, PostUpdateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/login/$', auth_views.LoginView),
    url(r'^account/logout/$', auth_views.LogoutView),
    url(r'^post/create/$', PostCreateView.as_view(), name='post-create'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', PostDeleteView.as_view(), name='post-delete'),
    url(r'^post/update/$', PostUpdateView.as_view(), name='post-update'),

    url(r'', include('poll.urls')),
]
