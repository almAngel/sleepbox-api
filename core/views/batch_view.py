from core.serializers.batch_serializer import BatchSerializer

@api_view(['POST'])
def upstream(request):
    if request.method == 'POST':
        serializer = BatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)