import pytest
from tests.utils.selenium_helpers import MoviesPage, MovieDetailsPage

APP_URL = "http://localhost:3000/"

def test_species_wookie_in_empire_strikes_back(driver):
    page = MoviesPage(driver)
    page.open(APP_URL)
    page.select_movie('The Empire Strikes Back')
    details = MovieDetailsPage(driver)
    species = details.get_species()
    assert any('Wookie' in s for s in species), "Wookie not found in species list"
    details.back()

def test_planet_camino_not_in_phantom_menace(driver):
    page = MoviesPage(driver)
    page.open(APP_URL)
    page.select_movie('The Phantom Menace')
    details = MovieDetailsPage(driver)
    planets = details.get_planets()
    assert all('Camino' not in p for p in planets), "Camino found in planets list"
    details.back()
