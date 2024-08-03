import requests

# Configurações da API

API_KEY = 'ea3bc29e6867e86363996f44deb7df08'

# Buscar filmes
filme = input('Digite um filme: ')

url = f"https://api.themoviedb.org/3/search/movie?query={filme}&include_adult=false&language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlYTNiYzI5ZTY4NjdlODYzNjM5OTZmNDRkZWI3ZGYwOCIsIm5iZiI6MTcyMjcwNDMwMS4zODA3NDMsInN1YiI6IjY2YWUzZTgzNTI4Y2E4YzgxMTQwZWU3NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.1bX1-m45zE4Zy9QPOnwgRQc3qvQFZBqt7amZg40J31U"
}


# Vizualizar filme
response = requests.get(url, headers=headers).json()
print(response)
for item in response:
    
    print(item[3])

# Adicionar na lista

# Sortear filmes da lista

# Mostrar filme sorteado e tirar da lista (Marcar como visto)