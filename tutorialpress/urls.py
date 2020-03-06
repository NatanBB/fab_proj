from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from tutorialpress.core.router import router as core_router

schema_view = get_schema_view(openapi.Info(title="Tutorialpress", default_version="v1"), public=True)

urlpatterns = [
    path("", include(core_router.urls)),
    path("admin/", admin.site.urls),
    path("swagger", schema_view.with_ui()),
]
