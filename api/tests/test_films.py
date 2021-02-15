from base import BaseTest
from enums.http_statuses import HttpStatus
from сonstants.test_data import WRONG_FILM_ID


class TestFilms(BaseTest):
    def test_get_all_films(self, films_steps):
        films_steps.get_all_films(status=HttpStatus.Ok)

    def test_get_film_positive(self, films_steps):
        films_steps.get_film(status=HttpStatus.Ok, film_id=1)

    def test_get_film_negative(self, films_steps):
        films_steps.get_film(status=HttpStatus.Not_Found, film_id=WRONG_FILM_ID)
