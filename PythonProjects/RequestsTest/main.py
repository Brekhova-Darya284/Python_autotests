import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '85a8b8a11ae92493169881b5431406ed'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

body_change = {
    "pokemon_id": "195471",
    "name": "Terry",
    "photo_id": 1
}

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

body_catch = {
    "pokemon_id": "195471"
}

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)

'''pokemon_id = response_create.json['id']
print(pokemon_id)'''