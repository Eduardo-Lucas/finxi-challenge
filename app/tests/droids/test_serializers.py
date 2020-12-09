from droids.serializers import PecaSerializer


def test_valid_peca_serializer():
    valid_serializer_data = {
        "codigo": "123456",
        "descricao": "Eixo Dianteiro",
        "importada": "Não"
    }
    serializer = PecaSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_peca_serializer():
    invalid_serializer_data = {
        "codigo": "456789",
        "importada": "Não"
    }
    serializer = PecaSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"descricao": ["This field is required."]}
