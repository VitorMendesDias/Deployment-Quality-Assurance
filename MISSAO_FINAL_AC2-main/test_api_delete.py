import requests

def test_delete_post():
    url = 'https://jsonplaceholder.typicode.com/posts/1'  # Deletando o post com ID 1

    # Fazendo a solicitação DELETE para remover o post, ignorando a verificação SSL
    response = requests.delete(url, verify=False)

    # Valida o status code da resposta
    assert response.status_code == 400