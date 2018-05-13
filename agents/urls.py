from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('read',views.read, name='read'),
    path('run',views.run, name='run'),
    path('delete',views.delete, name='delete'),
    path('see', views.see, name='see'),
    path('errorDB', views.errorDB, name='errorDB'),
]