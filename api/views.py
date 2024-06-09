from rest_framework import generics, status
from rest_framework.response import Response

from api.helpers import generate_short_code, create_full_url
from api.in_memory import UrlMap
from api.serializers import OriginalUrlSerializer


URL_MAP: UrlMap = UrlMap()


class EncodeOriginalUrlToShortenedUrlView(generics.CreateAPIView):
    serializer_class = OriginalUrlSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not (original_url := request.data.get("original_url")):
            return Response(data={"original_url": original_url}, status=status.HTTP_400_BAD_REQUEST)

        short_code: str = generate_short_code()
        while URL_MAP.key_exists(key=short_code):
            short_code = generate_short_code()

        URL_MAP.add_key(key=short_code, value=original_url)
        return Response(data={"shortened_url": create_full_url(short_code=short_code)}, status=status.HTTP_201_CREATED)
