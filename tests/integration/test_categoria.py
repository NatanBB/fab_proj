import pytest
from django.urls import reverse
from rest_framework import status

from tutorialpress.core.models import Categoria


@pytest.mark.django_db
def test_create_valid(api_client):
    # DADO dados de categoria válidos.
    dados_categoria = {"nome": "Categoria A"}

    # QUANDO a API é chamada para criar uma categoria.
    resp = api_client.post(reverse("categoria-list"), dados_categoria)

    # ENTÃO a reposta de sucesso deve conter os dados da categoria
    assert resp.status_code == status.HTTP_201_CREATED
    assert isinstance(resp.data["id"], int)

    # E ENTÃO a categoria deve existir no banco.
    assert Categoria.objects.get(pk=resp.data["id"]).nome == dados_categoria["nome"]


@pytest.mark.django_db
def test_create_invalid(api_client):
    dados_categoria = {"campo_invalido": "123"}
    resp = api_client.post(reverse("categoria-list"), dados_categoria)

    assert resp.status_code == status.HTTP_400_BAD_REQUEST
    assert len(resp.data["nome"]) != 0

    assert Categoria.objects.count() == 0


@pytest.mark.django_db
def test_retrieve_valid(api_client):
    dados_categoria = {"nome": "Categoria A"}

    resp = api_client.post(reverse("categoria-list"), dados_categoria)
    resp = api_client.get("/categorias/1/")

    assert resp.status_code == status.HTTP_200_OK
    assert isinstance(resp.data["id"], int)
    assert resp.data["nome"] == "Categoria A"


@pytest.mark.django_db
def test_update(api_client):
    dados_categoria = {"nome": "Categoria A"}
    novosDados = {"nome": "Categoria B"}
    resp = api_client.post(reverse("categoria-list"), dados_categoria)
    endResp = api_client.put(reverse("categoria-detail", args=[resp.data["id"]]), novosDados)

    assert endResp.status_code == status.HTTP_200_OK
    assert Categoria.objects.get(pk=resp.data["id"]).nome == novosDados["nome"]


@pytest.mark.django_db
def test_delete(api_client):
    dados_categoria = {"nome": "Categoria A"}
    resp = api_client.post(reverse("categoria-list"), dados_categoria)
    endDel = api_client.delete(reverse("categoria-detail", args=[resp.data["id"]]))

    assert endDel.status_code == status.HTTP_204_NO_CONTENT
    assert Categoria.objects.count() == 0
