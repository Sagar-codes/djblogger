import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db


class TestHomePage:
    def test_homepage_url(self, client):
        url = reverse('home') # to get the home url
        response = client.get(url) # client will surf the home page and return the response
        assert response.status_code==200  # raise assertion of the response



    def test_post_htmx_fragment(self, client):
        headers = {
            "HTTP_HX-Request" : "true"
        }
        url = reverse('home')
        response = client.get(url, **headers)
        assertTemplateUsed(response, "blog/components/post-list-elements.html")