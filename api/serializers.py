from django.core.validators import URLValidator
from rest_framework import serializers

from api.constants import MAX_LENGTH_ORIGINAL_URL, MAX_LENGTH_SHORTENED_URL


class OriginalUrlSerializer(serializers.Serializer):
    original_url = serializers.CharField(max_length=MAX_LENGTH_ORIGINAL_URL, validators=[URLValidator()])


class ShortenedUrlSerializer(serializers.Serializer):
    shortened_url = serializers.CharField(max_length=MAX_LENGTH_SHORTENED_URL, validators=[URLValidator()])
