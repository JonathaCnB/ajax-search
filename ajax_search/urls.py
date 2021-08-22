from ajax_app.views import detail_series, main_view, search_result
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_view, name="index"),
    path("search-result/", search_result, name="search_result"),
    path("series-detail/<int:pk>/", detail_series, name="series_detail"),
]
