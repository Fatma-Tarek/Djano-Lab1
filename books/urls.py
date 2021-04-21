from django.urls import path
from . import views # mean speak any method of views

# name important bs . if I change path 
urlpatterns = [
    path("",views.index,name="index"),
    path("create",views.create,name="create"),
    path("edit/<int:id>",views.edit,name="edit"),
    path("delete/<int:id>",views.delete,name="delete"),
]