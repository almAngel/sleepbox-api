from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from core.models.hello import Hello
from rest_framework.decorators import api_view

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!"})