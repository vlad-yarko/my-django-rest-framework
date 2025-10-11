from django.urls import path
from . import views


urlpatterns = [
    # path("", views.UserAPIView.as_view(), name="api_user")
    path("", views.VasyaView.as_view(), name="vasya")
]

