from faulthandler import is_enabled
import re
from rest_framework import serializers

class CreateURLShortenSerializer(serializers.Serializer):
    origin = serializers.URLField(required=True, allow_null=False, allow_blank=False, max_length=512)

class DeleteURLShortenSerializer(serializers.Serializer):
    secret_slug = serializers.CharField(required=True, allow_null=False, allow_blank=False)

class UpdateURLShortenSerializer(serializers.Serializer):
    secret_slug = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    origin = serializers.URLField(required=False)
    is_enabled = serializers.BooleanField(required=False)
