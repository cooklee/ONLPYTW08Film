import pytest

from movie.models import Actor


@pytest.fixture
def actors():
    lst = []
    for i in range(10):
        a = Actor.objects.create(first_name=i,
                                 last_name=i)
        lst.append(a)
    return lst
