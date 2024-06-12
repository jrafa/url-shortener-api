import json

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from url_shortener.settings import DOMAIN_URL


def create_shortened_url(api_client: APIClient, original_url: str):
    url = reverse("encode_to_shortened_url")
    data = {
        "original_url": original_url,
    }
    return api_client.post(path=url, data=data, format="json")


def test_encode_original_url_to_shortened_url_with_success(api_client):
    response = create_shortened_url(api_client=api_client, original_url="http://example.com")

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data is not None
    assert response.data["shortened_url"] is not None


@pytest.mark.parametrize("original_url", [None, "", "abc://hello.com"])
def test_encode_original_url_to_shortened_url_with_bad_request_no_success(api_client, original_url):
    response = create_shortened_url(api_client=api_client, original_url=original_url)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_decode_shortened_url_to_original_url_with_success(api_client):
    response_shortened_url = create_shortened_url(api_client=api_client, original_url="https://example.com").data
    url = reverse("decode_to_original_url")
    data = {
        "shortened_url": response_shortened_url["shortened_url"],
    }
    response = api_client.generic(method="GET", path=url, data=json.dumps(data), content_type="application/json")

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {"original_url": "https://example.com"}


@pytest.mark.parametrize("shortened_url", [None, "", "abc://hello.com"])
def test_decode_shortened_url_to_original_url_with_bad_request_no_success(api_client, shortened_url):
    url = reverse("decode_to_original_url")
    data = {
        "shortened_url": shortened_url,
    }
    response = api_client.generic(method="GET", path=url, data=json.dumps(data), content_type="application/json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_decode_shortened_url_to_original_url_with_not_found(api_client):
    url = reverse("decode_to_original_url")
    data = {
        "shortened_url": f"{DOMAIN_URL}/xyz1234",
    }
    response = api_client.generic(method="GET", path=url, data=json.dumps(data), content_type="application/json")

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_redirect_view_shortened_url_to_original_url_with_success(api_client):
    response_shortened_url = create_shortened_url(api_client=api_client, original_url="https://example.com").data
    short_code = response_shortened_url["shortened_url"].split("/")[-1]
    url = reverse("redirect_to_original_url", kwargs={"short_code": short_code})
    response = api_client.get(path=url, format="json")

    assert response.status_code == status.HTTP_302_FOUND


def test_redirect_view_shortened_url_to_original_url_with_not_found(api_client):
    url = reverse("redirect_to_original_url", kwargs={"short_code": "NoEx123"})
    response = api_client.get(path=url, format="json")

    assert response.status_code == status.HTTP_404_NOT_FOUND
