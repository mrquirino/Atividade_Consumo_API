import requests

url = 'https://viacep.com.br/ws/MG/Belo Horizonte/Rua dos Aimores/json'

r = requests.get(url)

if r.status_code == 200:
    dados = r.json()
    for item in dados:
        print(item)
        print()
else:
    print('Não houve sucesso na requisão.')