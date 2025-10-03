from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()

router.register(r"viewset_cucumber", views.CucumberViewSet, basename="viewset_cucumber")


urlpatterns = [
    path("api_cucumber/", views.CucumberAPIView.as_view(), name="api_cucumber"),
    path("api_cucumber/<int:pk>/", views.CucumberAPIView.as_view(), name="api_cucumber_one"),
    
    path("generics_cucumber/", views.CucumberListCreateGenericsView.as_view(), name="generics_cucumber"),
    path("generics_cucumber/<int:pk>/", views.CucumberRetrieveUpdateDestroyGenericsView.as_view(), name="generics_cucumber_one"),
    
    path("", include(router.urls))
]
