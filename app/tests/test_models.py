import pytest

from droids.models import Peca


@pytest.mark.django_db
def test_peca_model():
    peca = Peca(codigo="123456", descricao="Rebimboca da Parafuseta", importada="Sim")
    peca.save()
    assert peca.codigo == "123456"
    assert peca.descricao == "Rebimboca da Parafuseta"
    assert peca.importada == "Sim"
    assert peca.data_cadastro
    assert peca.data_alteracao
    assert str(peca) == peca.descricao
