import pytest
from http_api.models import Session


@pytest.mark.django_db 
def test_session_count():
    assert Session.objects.count() == 0
