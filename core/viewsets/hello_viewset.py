from core.models.hello import Hello
from django.shortcuts import get_object_or_404
from core.serializers.hello_serializer import HelloSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class HelloViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving hello.
    """

    # queryset = Hello.objects.all
    serializer_class = HelloSerializer

    @action(detail=True, methods=['get'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = HelloSerializer(data=request.data)
        return Response({'content': 'Hello World!!'})