from django.urls import path

from . import views

urlpatterns = [
        path('createuser', views.createUser),
        path('login', views.login),
        path('session', views.checksession),   # Your mapping must be in follwing format
            # path('', views.viewname, name='somename'),
            ]
