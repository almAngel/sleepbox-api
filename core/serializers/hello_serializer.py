from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=200)