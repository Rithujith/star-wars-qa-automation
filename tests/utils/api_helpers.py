import requests

BASE_URL = 'https://swapi.dev/api/films/'

def get_movies():
    response = requests.get(BASE_URL)
    response.raise_for_status()
    return response.json()['results']

def get_movie_by_index(index):
    movies = get_movies()
    return movies[index]
