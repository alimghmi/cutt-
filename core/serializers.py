from faulthandler import is_enabled
from rest_framework import serializers

class CreateURLShortenSerializer(serializers.Serializer):
    origin = serializers.URLField(required=True, allow_null=False, allow_blank=False, max_length=512)

class DeleteURLShortenSerializer(serializers.Serializer):
    slug = serializers.CharField(required=True, allow_null=False, allow_blank=False)
