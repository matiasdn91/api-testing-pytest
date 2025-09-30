# Test que verifica el comportamiento de un endpoint inválido, debe devolver un código 404
def test_invalid_endpoint(get_response):
    response = get_response("/breed/invalid_breed/images/random")
    assert response.status_code == 404