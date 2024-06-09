from rest_framework import generics, status
from rest_framework.response import Response

from api.helpers import generate_short_code, create_full_url
from api.in_memory import UrlMap
from api.serializers import OriginalUrlSerializer, ShortenedUrlSerializer

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


class DecodeShortenedUrlToOriginalUrlView(generics.GenericAPIView):
    serializer_class = ShortenedUrlSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not (shortened_url := request.data.get("shortened_url")):
            return Response(data={"shortened_url": shortened_url}, status=status.HTTP_400_BAD_REQUEST)

        short_code: str = shortened_url.split("/")[-1]
        if URL_MAP.key_not_exists(key=short_code):
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(data={"original_url": URL_MAP.get_value(key=short_code)}, status=status.HTTP_200_OK)
