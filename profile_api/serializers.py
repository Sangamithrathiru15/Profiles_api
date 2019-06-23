from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """serializes a name field for testing ourAPIView,also takes care of the validation"""
    name=serializers.CharField(max_length=10)
