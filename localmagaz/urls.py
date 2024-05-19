from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static


from localmagaz import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("catalog.urls", namespace="catalog")),
    path("cataloge/", include("goods.urls", namespace="cataloge")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
