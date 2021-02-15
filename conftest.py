import pytest

from support.files_reader import read_plugin_names, clean_working_dir

pytest_plugins = read_plugin_names()


def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line("markers",
                            "ignore_on(name): mark tests to ignore on specified environment")


@pytest.fixture(scope="session", autouse=True)
def clean_project_dir(request):
    def clean():
        clean_working_dir()
    request.addfinalizer(clean)
