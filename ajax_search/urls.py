from ajax_app.views import (
    detail_series,
    main_view,
    photo_add_view,
    search_result,
)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_view, name="index"),
    path("chat/", include("djangochat.urls")),
    path("upload-image/", photo_add_view, name="upload_image"),
    path("search-result/", search_result, name="search_result"),
    path("series-detail/<int:pk>/", detail_series, name="series_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
