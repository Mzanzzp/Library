import pytest
from autors.models import Autor

@pytest.fixture
def autors_fixture(db):
    return Autor.objects.create(name="jan", surname="dom", year_of_birth="1999-05-11")