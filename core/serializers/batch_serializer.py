
from rest_framework import serializers
import time

class BatchSerializer(serializers.Serializer):
    device_id = serializers.CharField(max_length=200)
    timestamp = serializers.IntegerField(allow_null=False, default=int(time.time()))