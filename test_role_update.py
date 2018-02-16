import requests

def test_init_role_created(app_url, init_role):
    response = requests.post(app_url + "roles/", data=init_role)
    assert response.status_code == 201


def test_role_update(app_url,role, init_role):
    role['name'] = 'Big bear'
    response = requests.put(app_url + 'roles/{}/'.format (init_role['id']), data=role)
    assert response.status_code == 200
    #assert response.json() == role
