import json

import allure
from hamcrest import assert_that, equal_to

from support.helper import is_json


@allure.step("Check request status: actual = {1}, expected = {2}")
def log_assert_status(logger, actual, expected):
    if expected != actual.status_code:
        if is_json(actual):
            logger.error("RESPONSE = " + json.dumps(actual.json(), indent=4, sort_keys=True, ensure_ascii=False))
            assert_that(actual.status_code, equal_to(expected))
        else:
            assert_that(actual.status_code, equal_to(expected))
    else:
        if is_json(actual):
            logger.info("RESPONSE = " + json.dumps(actual.json(), indent=4, sort_keys=True, ensure_ascii=False))
            assert_that(actual.status_code, equal_to(expected))
        else:
            assert_that(actual.status_code, equal_to(expected))
