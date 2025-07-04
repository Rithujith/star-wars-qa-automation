import pytest
from tests.utils.selenium_helpers import MoviesPage

APP_URL = "http://localhost:3000/"  # Change if running on a different port

def test_sort_movies_title(driver):
    page = MoviesPage(driver)
    page.open(APP_URL)
    page.sort_by('Title')
    titles = page.get_movie_titles()
    assert titles[-1] == 'The Phantom Menace', f"Expected last movie to be 'The Phantom Menace', got {titles[-1]}"
