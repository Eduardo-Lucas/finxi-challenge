import pytest

from droids.models import Peca


@pytest.fixture(scope='function')
def add_peca():
    def _add_peca(codigo, descricao, importada):
        peca = Peca.objects.create(codigo=codigo, descricao=descricao, importada=importada)
        return peca
    return _add_peca
