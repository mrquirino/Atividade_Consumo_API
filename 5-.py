import requests

r = requests.get('https://www.google.com/search', params={'q': 'elson de abreu'})

if (r.status_code == 200):
    with open("resultado_google.html", "w", encoding="UTF-8") as f:
        f.write(r.text)
    print("Resultado salvo em 'resultado_google.html'")
else:
    print('Não houve sucesso na requisão.')