from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r"students", views.StudentViewSet, basename="students_viewset")
router.register(r"courses", views.CourseViewSet, basename="courses_viewset")


urlpatterns = [
    path("", include(router.urls))
]

