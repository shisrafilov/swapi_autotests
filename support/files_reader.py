import argparse
import fnmatch
import functools
import glob
import os
import shutil

import yaml

from definitions import CONFIG_PATH, ROOT_DIR
from support.decorator import func_once


class StringConcatinator(yaml.YAMLObject):
    yaml_loader = yaml.SafeLoader
    yaml_tag = '!join'

    @classmethod
    def from_yaml(cls, loader, node):
        return functools.reduce(lambda a, b: a.value + b.value, node.value)


@func_once
def get_args():
    parser = argparse.ArgumentParser(argument_default=None)
    parser.add_argument('--profile', '-p', help='set active profile', dest='profile')
    parser.add_argument('--alluredir', '-ad', help='set allure directory', dest='alluredir', required=False)
    return parser.parse_known_args()[0]  # return only recognised values


@func_once
def app_config():
    with open(CONFIG_PATH, 'rt') as ymlfile:
        cfg = yaml.safe_load(ymlfile.read())
    return cfg


def recursive_glob(treeroot, pattern):
    results = []
    for base, dirs, files in os.walk(treeroot):
        good_files = fnmatch.filter(files, pattern)
        results.extend(os.path.join(base, f) for f in good_files)
    return results


def read_plugin_names():
    pattern = '*_fixture.py'
    fixture_paths = recursive_glob(ROOT_DIR, pattern)

    plugins = []
    for i, name in enumerate(fixture_paths):
        fixture_paths[i] = name.replace(name, name[:-3])
        fixture_paths[i] = fixture_paths[i].split(os.path.sep)
        plugins.append(fixture_paths[i][-3] + "." + fixture_paths[i][-2] + "." + fixture_paths[i][-1])
    return plugins


def clean_working_dir():
    clean_files = './build ./dist ./*.pyc ./*.tgz ./*.egg-info'.split(' ')

    for path_spec in clean_files:
        # Make paths absolute and relative to this path
        abs_paths = glob.glob(os.path.normpath(os.path.join(ROOT_DIR, path_spec)))
        for path in [str(p) for p in abs_paths]:
            if not path.startswith(ROOT_DIR):
                # Die if path in CLEAN_FILES is absolute + outside this directory
                raise ValueError("%s is not a path inside %s" % (path, ROOT_DIR))
            print('removing %s' % os.path.relpath(path))
            shutil.rmtree(path)
