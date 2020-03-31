
from rest_framework import serializers
from core.models.batch import Batch
import time

class BatchSerializer(serializers.Serializer):
    device_id = serializers.CharField(max_length=200)
    timestamp = serializers.IntegerField(allow_null=False, default=int(time.time()))

    def create(self, validated_data):
        print(validated_data)
        return Batch(**validated_data)