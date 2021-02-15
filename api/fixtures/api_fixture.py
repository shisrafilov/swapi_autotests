import pytest

from api.steps.films_steps import FilmsSteps
from base import BaseApiClient


@pytest.fixture
def films_steps():
    return FilmsSteps(BaseApiClient())
