# Test que verifica que la API devuelva la lista completa de razas
def test_list_all_breeds(get_response):
    response = get_response("/breeds/list/all")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert isinstance(data["message"], dict)
    assert "hound" in data["message"]

# Test que verifica que un endpoint de sub-razas devuelve correctamente la lista
def test_hound_sub_breeds(get_response):
    response = get_response("/breed/hound/list")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert isinstance(data["message"], list)
    assert "afghan" in data["message"]