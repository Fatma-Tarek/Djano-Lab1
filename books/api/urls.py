from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("login",obtain_auth_token),
    path("signup",views.api_signup),
    path("view/<int:id>",views.view),
    path("destroy/<int:id>",views.destroy),
    path("update/<int:id>",views.update),
    path("",views.index),
    path("create",views.create),
    

]