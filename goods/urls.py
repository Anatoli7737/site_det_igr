from django.urls import path, include

from goods import views

app_name = "goods"

urlpatterns = [
    path("", views.cataloge, name="index"),
    path("product/", views.product, name="product"),
]
