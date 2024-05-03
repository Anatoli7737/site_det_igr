from django.urls import path, include

from catalog import views

app_name = "catalog"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("dostavka/", views.dostavka, name="dostavka"),
    path("inform/", views.inform, name="inform"),
]
