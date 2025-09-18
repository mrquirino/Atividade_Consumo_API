import requests

url = 'https://viacep.com.br/ws/'
formato = '/json/'

cep_base = 30140071

for i in range(5):
    cep = str(cep_base + i)
    r = requests.get(url + cep + formato)

    if r.status_code == 200:
        print(f"CEP {cep} -> ", r.json())
        print()
    else:
        print(f"Falha na consulta do CEP {cep}")
