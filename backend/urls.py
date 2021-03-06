"""backend URL Configuration

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
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
#from .views import index
from .views import acme_challenge
from todo.views import  TodoView

router = routers.DefaultRouter()
router.register(r'todos', TodoView, 'todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('.well-known/acme-challenge/-mUIvSiRb6mlZG7n_7Ef7MLsClSyVZhRXtajJBo0SH0', acme_challenge, name='acme-challenge'),
    #re_path(r'^', index, name='index'),
    re_path(r'^auth/', include('authentication.urls')),
]
