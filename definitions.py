import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, 'application.yaml')
LOGGER_CONF_PATH = os.path.join(ROOT_DIR, 'logger', 'log.yaml')
REQUIREMENTS = os.path.join(ROOT_DIR, 'requirements.txt')
