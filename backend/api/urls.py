"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView
from .views import contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', contact_view, name='contact'),
    path('register/', views.register, name='register'),
    path('insertuser', views.insertuser, name='insertuser'),
    path('events', views.events, name='events'),
    path('events/<int:festival_id>/', views.eventdetail, name='eventdetail'),
    path('events/<int:festival_id>/book/', views.booktickets, name='booktickets'),
    path('signin/', views.signin, name='signin'),
    path('custom_login', views.custom_login, name='custom_login'),
    path('booking', views.booking, name='booking'),
    path('search', views.search, name='search'),
    path('logout/', views.logout, name='logout'),
    path('ticket_prices/', views.ticket_prices, name='ticket_prices'),
    path('mybookings/', views.mybookings, name='mybookings'),
    path('', include('django_prometheus.urls')),  # Exposes /metrics endpoint
]