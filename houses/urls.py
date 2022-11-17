from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('catalog/', catalog, name='catalog'),
    path('search/', housesSearch.as_view(), name='houseSearch'),
    path('login/', userLogin, name='userLogin'),
    path('register/', userRegister, name='userRegister'),
]