from django.urls import path
from .views import *

urlpatterns = [
    path("",main,name="main"),
    path("kassa",kassa,name="kassa"),
    path("zakupki",zakupki,name="zakupki"),
    path("kassa/list",get_kassa,name="get_kassa"),
    path("login",Login.as_view(),name="login"),
    path("logout",logout_user,name="logout"),
]
