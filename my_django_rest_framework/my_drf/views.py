from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .serializers import CucumberSerializer, ModelCucumberSerializer
from .models import Cucumber


cucumber_path_pk_param = openapi.Parameter(
    "cucumber_id",
    openapi.IN_PATH,
    description="ID of a cucumber",
    type=openapi.TYPE_INTEGER
)


class CucumberAPIView(APIView):
    
    @swagger_auto_schema(
        operation_description="Get server info",
        tags=["Cucumber"],
        manual_parameters=[cucumber_path_pk_param],
        responses={
            200: openapi.Response(
                description="Cucumber data",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'title': openapi.Schema(type=openapi.TYPE_STRING)
                    },
                ),
                # examples={
                #     "application/json": {  # Must include content type
                #         "title": "Cucumber"
                #     }
                # }
            ),
            404: openapi.Response(
                description="Cucumber not found",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={'error': openapi.Schema(type=openapi.TYPE_STRING)}
                ),
                # examples={
                #     "application/json": {  # Must include content type
                #         "error": "Cucumber not found"
                #     }
                # }
            )
        }
    )
    def get(self, request: Request, pk=None):
        if pk:
            try:
                cucumber = Cucumber.objects.get(id=pk)
            except Exception:
                return Response({"error": "No cucumber"}, status=status.HTTP_404_NOT_FOUND)
            serializer = CucumberSerializer(cucumber)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            cucumbers = Cucumber.objects.all()
            serializer = CucumberSerializer(cucumbers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request: Request):
        serializer = CucumberSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    def put(self, request: Request, pk):
        try:
            cucumber = Cucumber.objects.get(id=pk)
        except Exception:
            return Response({"message": "No cucumber"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CucumberSerializer(cucumber, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    def patch(self, request: Request, pk):
        try:
            cucumber = Cucumber.objects.get(id=pk)
        except Exception:
            return Response({"message": "No cucumber"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CucumberSerializer(cucumber, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    def delete(self, request: Request, pk):
        try:
            cucumber = Cucumber.objects.get(id=pk)
        except Exception:
            return Response({"message": "No cucumber"}, status=status.HTTP_404_NOT_FOUND)
        cucumber.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CucumberListCreateGenericsView(generics.ListCreateAPIView):
    queryset = Cucumber.objects.all()
    serializer_class = ModelCucumberSerializer
    lookup_field = "pk"


class CucumberRetrieveUpdateDestroyGenericsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cucumber.objects.all()
    serializer_class = ModelCucumberSerializer
    lookup_field = "pk"
    
    
class CucumberViewSet(viewsets.ModelViewSet):
    queryset = Cucumber.objects.all()
    serializer_class = ModelCucumberSerializer
    lookup_field = "pk"

