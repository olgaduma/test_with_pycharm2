import requests


def test_role_update(app_url, role):
    role['name'] = 'Big bear'
    response = requests.put(app_url + 'roles/{}/'.format (role['id']), data=role)
    assert response.status_code == 200
    #assert response.json() == role
