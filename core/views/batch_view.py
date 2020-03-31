
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from core.models.hello import Hello
from rest_framework.decorators import api_view
from core.serializers.batch_serializer import BatchSerializer

@api_view(['POST'])
def upstream(request):
    if request.method == 'POST':
        serializer = BatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)