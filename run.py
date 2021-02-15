from setuptools import setup, find_packages

from definitions import REQUIREMENTS


def get_requirements():
    with open(REQUIREMENTS, "r", encoding='UTF-8') as requirements:
        array = []
        for line in requirements:
            array.append(str(line.rstrip()))
        return array


setup(
    setup_requires=["pytest-runner"],
    install_requires=get_requirements(),
    packages=find_packages(),
    name='swapi_autotests'
)
