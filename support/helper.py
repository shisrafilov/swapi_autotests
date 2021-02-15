import logging

import requests

from support.decorator import func_once

logger = logging.getLogger(__name__)


def join_url_paths(*args):
    """Joins given arguments into a url. Trailing but not leading slashes are stripped for each argument. """
    return "/".join(map(lambda x: str(x).rstrip('/'), args))


def is_json(obj):
    try:
        obj.json()
    except ValueError:
        return False
    return True


@func_once
def session():
    return requests.Session()
