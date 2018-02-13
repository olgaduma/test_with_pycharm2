import requests

def test_role_created(app_url, role):
    print(role["book"])
    response = requests.post(app_url + "roles/", data=role)
    assert response.status_code == 201
