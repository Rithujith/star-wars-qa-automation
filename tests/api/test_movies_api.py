import pytest
from tests.utils.api_helpers import get_movies, get_movie_by_index

def test_movies_count():
    movies = get_movies()
    assert len(movies) == 6, f"Expected 6 movies, got {len(movies)}"

def test_third_movie_director():
    movie = get_movie_by_index(2)  # 3rd movie, 0-based index
    assert movie['director'] == 'Richard Marquand', f"Expected director Richard Marquand, got {movie['director']}"

def test_fifth_movie_producers():
    movie = get_movie_by_index(4)  # 5th movie
    assert movie['producer'] != 'Gary Kurtz, George Lucas', "Producers should not be Gary Kurtz, George Lucas"
