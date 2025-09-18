import requests

url = 'https://viacep.com.br/ws/abc/'

r = requests.get(url)

print()
print("Código de Retorno:", r.status_code)
print()
print('Texto da resposta:', r.text)