
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from core.models.batch import Batch
from rest_framework.decorators import api_view
from core.serializers.batch_serializer import BatchSerializer
from core.tools import firebase_client

@api_view(['GET', 'POST'])
def upstream(request):
    
    if request.method == 'GET':
        return Response({"message": "Batch get"})
    elif request.method == 'POST':
        serializer = BatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            client = firebase_client.FirebaseClient()
            client.collection("batches").add(serializer.data)

            print(serializer.data)

            return Response(
                { 
                    "message": f"Box (id={serializer.data['device_id']}) batch uploaded correctly",
                    "status": 201
                }, 
                status=201
            )