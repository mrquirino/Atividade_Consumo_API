import requests

url = 'https://viacep.com.br/ws/'
cep = '30140071'
formato = '/json'

r = requests.get(url + cep + formato)

if (r.status_code == 200):
    print()
    print('JSON : ', r.json())
    print()
else:
    print('Não houve sucesso na requisão.')