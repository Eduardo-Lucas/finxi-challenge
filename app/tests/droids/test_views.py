import json

import pytest

from droids.models import Peca


@pytest.mark.django_db
def test_add_peca(client):
    pecas = Peca.objects.all()
    assert len(pecas) == 0

    resp = client.post(
        "/api/pecas/",
        {
            "codigo": "123456",
            "descricao": "Rebimboca da Parafuseta",
            "importada": "Não",
        },
        content_type="application/json"
    )
    assert resp.status_code == 201
    assert resp.data["descricao"] == "Rebimboca da Parafuseta"

    pecas = Peca.objects.all()
    assert len(pecas) == 1


@pytest.mark.django_db
def test_add_peca_invalid_json(client):
    pecas = Peca.objects.all()
    assert len(pecas) == 0

    resp = client.post(
        "/api/pecas/",
        {},
        content_type="application/json"
    )
    assert resp.status_code == 400

    pecas = Peca.objects.all()
    assert len(pecas) == 0


@pytest.mark.django_db
def test_add_peca_invalid_json_keys(client):
    pecas = Peca.objects.all()
    assert len(pecas) == 0

    resp = client.post(
        "/api/pecas/",
        {
            "codigo": "898989",
            "importada": "Sim",
        },
        content_type="application/json"
    )
    assert resp.status_code == 400

    pecas = Peca.objects.all()
    assert len(pecas) == 0


@pytest.mark.django_db
def test_get_single_peca(client, add_peca):
    peca = add_peca(codigo="787878", descricao="Alfinete", importada="Sim")
    resp = client.get(f"/api/pecas/{peca.id}/")
    assert resp.status_code == 200
    assert resp.data["descricao"] == "Alfinete"


def test_get_single_peca_incorrect_id(client):
    resp = client.get(f"/api/pecas/foo/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_all_pecas(client, add_peca):
    peca_one = add_peca(codigo="909090", descricao="Lanterna dianteira esquerda", importada="Não")
    peca_two = add_peca("808080", "Limpador de parabrisa traseiro", "Não")
    resp = client.get(f"/api/pecas/")
    assert resp.status_code == 200
    assert resp.data[0]["descricao"] == peca_one.descricao
    assert resp.data[1]["descricao"] == peca_two.descricao
