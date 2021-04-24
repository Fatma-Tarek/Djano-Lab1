from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("login",obtain_auth_token),
    path("",views.index),
    path("create",views.create),

]