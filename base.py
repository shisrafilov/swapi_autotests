from logger.logger import prepared_logger
from support.files_reader import app_config
from support.helper import join_url_paths
from support.helper import session

configuration = app_config()


class BaseTest(object):
    logger = prepared_logger()


class BaseSteps(object):
    def __init__(self, client):
        """Constructor.
        Args:
            client (object): client for resources manipulation.
        """
        self.client = client
        self.config = configuration
        self.logger = prepared_logger()


class BaseApiClient:
    """Base API Client."""
    @property
    def url(self):
        """Get base_url for each client type.
        Returns:
            object: url.
        """
        return configuration['url']

    def get(self, url=None, params=None, **kwargs):
        """Get request to API."""
        url = (lambda x: self.url if x is None else join_url_paths(self.url, url))(url)
        return session().get(url, params=params, **kwargs)
