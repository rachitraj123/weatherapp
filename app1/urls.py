from django.urls import path
from . import views


appname = 'app1'


urlpatterns = [
    path('',views.index,name = 'index'),
]