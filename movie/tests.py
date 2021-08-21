import pytest
# Create your tests here.
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_index_view():
    c = Client()
    response = c.get("/")
    movies = response.context['object_list']
    assert movies.count() == 0
    assert response.status_code == 200

@pytest.mark.django_db
def test_actor_list_view(actors):
    c = Client()
    url = reverse('list_actor')
    response = c.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(actors)
    for actor in actors:
        assert actor in response.context['object_list']

