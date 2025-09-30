import pytest

# Test básico: obtener una imagen aleatoria de cualquier perro
def test_random_dog_image(get_response):
    response = get_response("/breeds/image/random")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"].startswith("http")

# Test parametrizado: obtener imágenes aleatorias de varias razas
@pytest.mark.parametrize("breed", ["hound", "pug", "bulldog"])
def test_random_image_by_breed(get_response, breed):
    response = get_response(f"/breed/{breed}/images/random")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"].startswith("http")

# Test de consistencia: asegurar que dos imágenes aleatorias no sean iguales
@pytest.mark.parametrize("breed", ["hound", "pug"])
def test_random_images_are_different(get_response, breed):
    url = f"/breed/{breed}/images/random"
    response1 = get_response(url)
    response2 = get_response(url)
    assert response1.status_code == 200
    assert response2.status_code == 200
    data1 = response1.json()
    data2 = response2.json()
    assert data1["message"] != data2["message"]