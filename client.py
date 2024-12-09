import requests

url = "http://127.0.0.1:8000/utilisateurs/"
data = {"nom": "Alice", "age": 30}

response = requests.post(url, json=data)

if response.status_code == 200:
    print(response.json())  # Affiche l'utilisateur créé
else:
    print(f"Erreur : {response.status_code}")