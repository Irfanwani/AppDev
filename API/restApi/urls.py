from django.urls import path
from . import views

appname = 'restApi'

urlpatterns = [
    path('', views.index, name='index')
]