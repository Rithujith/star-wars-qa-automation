from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MoviesPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def sort_by(self, column_name):
        # Click the header to sort by column
        header = self.driver.find_element(By.XPATH, f"//th[contains(., '{column_name}')]")
        header.click()

    def get_movie_titles(self):
        # Returns a list of movie titles in the table
        return [el.text for el in self.driver.find_elements(By.XPATH, "//tbody//tr/td[1]")]

    def select_movie(self, movie_title):
        row = self.driver.find_element(By.XPATH, f"//tr[td[contains(., '{movie_title}')]]")
        row.click()

class MovieDetailsPage:
    def __init__(self, driver):
        self.driver = driver

    def get_species(self):
        return [el.text for el in self.driver.find_elements(By.XPATH, "//section[contains(., 'Species')]//li")]

    def get_planets(self):
        return [el.text for el in self.driver.find_elements(By.XPATH, "//section[contains(., 'Planets')]//li")]

    def back(self):
        self.driver.find_element(By.XPATH, "//button[contains(., 'Back')]").click()
