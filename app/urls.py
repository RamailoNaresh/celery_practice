from django.urls import path
from . import views


urlpatterns = [
    path("", views.addingNum, name="add-num"),
    path("get_all/", views.getallObj, name="get obj")
]
