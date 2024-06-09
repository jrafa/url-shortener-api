"""
URL configuration for url_shortener project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from api.views import (
    EncodeOriginalUrlToShortenedUrlView,
    DecodeShortenedUrlToOriginalUrlView,
    RedirectShortenedUrlToOriginalUrlView,
)

urlpatterns = [
    path("<str:short_code>", RedirectShortenedUrlToOriginalUrlView.as_view(), name="redirect_to_original_url"),
    path("decode/", DecodeShortenedUrlToOriginalUrlView.as_view(), name="decode_to_original_url"),
    path("encode/", EncodeOriginalUrlToShortenedUrlView.as_view(), name="encode_to_shortened_url"),
]
