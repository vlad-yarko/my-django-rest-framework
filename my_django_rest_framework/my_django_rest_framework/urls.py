"""
URL configuration for my_django_rest_framework project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from rest_framework.schemas import get_schema_view
# from rest_framework.documentation import include_docs_urls
# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view


schema_view = swagger_get_schema_view(
    openapi.Info(
        title="My DRF",
        default_version="1.0.0",
        description="My DRF docs",
        terms_of_service="https://github.com/vlad-yarko/",
        contact=openapi.Contact(email="mister_business@gmail.com"),
        license=openapi.License(name="BSD License")
    ),
    public=True
)

    
urlpatterns = [
    path("my-drf/", include("my_drf.urls")),
    path("homework/", include("homework.urls")),
    path('admin/', admin.site.urls),
    
    path("docs/", schema_view.with_ui('swagger', cache_timeout=0), name="docs"),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc')
    
    # path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    # path("schema/", get_schema_view(
    #     title="DRF",
    #     description="My DRF",
    #     version="1.0.0"
    # ), name="schema"),
    
    # path("docs/", include_docs_urls(
    #     title="DRF"
    # ))
    # path("drf", include("drf.urls"))
]
