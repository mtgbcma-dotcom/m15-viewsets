from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="api:api-root", permanent=False)),
    path("admin/", admin.site.urls),
    path("api/", include(("api.urls", "api"), namespace="api")),
    path("api-auth/", include("rest_framework.urls")),
]
