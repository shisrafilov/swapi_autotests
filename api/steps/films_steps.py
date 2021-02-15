import inspect

import allure
from schematics.validate import validate

from base import BaseSteps
from enums.http_statuses import HttpStatus
from models.errors import NotFound
from models.films import Films, Film
from support.asserts import log_assert_status
from support.helper import join_url_paths
from сonstants.request_constants import FILMS


class FilmsSteps(BaseSteps):
    @allure.step('get list of all films')
    def get_all_films(self, status):
        self.logger.info(f"Step: {inspect.currentframe().f_code.co_name} started")
        response = self.client.get(url=FILMS)
        log_assert_status(self.logger, response, status)
        if status == HttpStatus.Ok:
            validate(Films(), response.json())
        self.logger.info(f"Step: {inspect.currentframe().f_code.co_name} done")
        return response

    @allure.step('get one specific film')
    def get_film(self, status, film_id):
        self.logger.info(f"Step: {inspect.currentframe().f_code.co_name} started")
        response = self.client.get(url=join_url_paths(FILMS, film_id))
        log_assert_status(self.logger, response, status)
        content = response.json()
        if status == HttpStatus.Ok:
            validate(Film(), content)
        elif status == HttpStatus.Not_Found:
            validate(NotFound(), content)
        else:
            raise Exception(f'Invalid status: {status}')
        self.logger.info(f"Step: {inspect.currentframe().f_code.co_name} done")
        return response
