
from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('delete_links/', views.delete_links, name='delete_links'),
]