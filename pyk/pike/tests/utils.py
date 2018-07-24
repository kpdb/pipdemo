import os
import shutil
import tempfile


def make_tmpdir():
    return tempfile.mkdtemp()


def remove_dir(filename):
    if os.path.exists(filename):
        shutil.rmtree(filename)


def write_file(filename, content=''):
    with open(filename, 'w') as fp:
        fp.write(content)


def create_working_package(location, name=None):
    pkg_location = os.path.join(location, name or 'pike_tests')
    os.makedirs(pkg_location)
    write_file(os.path.join(pkg_location, '__init__.py'))

    return pkg_location
