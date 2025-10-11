from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# from .serializers import UserSerializer
# from .signals import mark_first_login

from .signals import vasya_signal

from google import genai



# class UserAPIView(APIView):
#     @swagger_auto_schema(
#         operation_description="Login user",
#         tags=["User"])    
#     def post(self, request: Request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             # take user
#             mark_first_login(request.user)
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    

class VasyaView(APIView):
    def get(self, request: Request):
        # vasya_signal.send(None)
        # return Response(data={"message": "ok"})
        
        client = genai.Client(api_key="AIzaSyDcSjAhFNfgg06LD7qFSPrwTYe8pB7kWj0")
    
        resp = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Vasya"
        )
        
        return Response(data={"message": resp.text})
        
