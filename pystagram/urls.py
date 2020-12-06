"""pystagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin, auth
from django.urls import path, re_path, include

from photos.views import ping
from photos.views import detail
from photos.views import create

urlpatterns = [
    path('', ping),
    path('admin/', admin.site.urls),
    re_path(r'^photos/(?P<pk>[0-9]+)/$', detail, name='detail'),
    re_path(r'^photos/upload/$', create, name='create'),
    # re_path(
    #     r'^accounts/login/',
    #     auth.login,
    #
    #     kwargs={'template_name': 'login.html'
    #             },
    #     name='login',
    # ),
    # re_path(
    #     r'^accounts/logout/',
    #     auth.logout,
    #     kwargs={
    #         'next_page': settings.LOGIN_URL,
    #     },
    #     name='logout',
    #
    # ),
    path('accounts/',include('django.contrib.auth.urls')),
]

urlpatterns += static('/upload_files/', document_root=settings.MEDIA_ROOT)
