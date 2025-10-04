from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ModelCourseSerializer, ModelStudentSerializer
from .models import Student, Course


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.prefetch_related("courses").all()
    serializer_class = ModelStudentSerializer
    lookup_field = "pk"
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["name"]
    search_fields = ["name"]
    ordering_fields = ["name"]

    
    
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.prefetch_related("students").all()
    serializer_class = ModelCourseSerializer
    lookup_field = "pk"
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["title"]
    search_fields = ["title"]
    ordering_fields = ["title"]
    
    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAdminUser()]
