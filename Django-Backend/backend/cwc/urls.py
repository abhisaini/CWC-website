from django.urls import path

from . import views

urlpatterns = [
        path('createuser', views.createUser),
        path('login', views.login),
        path('createpost', views.createPost),
        path('posts', views.getPosts),
        path('session', views.checksession),
        path('deletepost', views.deletePost),
          # Your mapping must be in follwing format
            # path('', views.viewname, name='somename'),
            ]
