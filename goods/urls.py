from django.urls import path

from goods import views


app_name = "goods"

urlpatterns = [
    path("search/", views.cataloge, name="search"),
    path("", views.cataloge, name="index"),
    path("product/<slug:product_slug>/", views.product, name="product"),
]
