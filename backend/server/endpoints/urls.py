from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from endpoints.views import (
    EndpointViewSet,
    MLAlgorithmViewSet,
    MLAlgorithmStatusViewSet,
    MLRequestViewSet,
    PredictView,
)

# Initialize the router
router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    re_path(r"^api/v1/(?P<endpoint_name>.+)/predict$", PredictView.as_view(), name="predict"),
]
