# coding=utf-8

import os
import sys
from setuptools import setup, find_packages

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from sdls import __version__


def package_data_dirs(source, basedir='/usr/share/sdls'):
    dirs = []

    for dirname, _, files in os.walk(source):
        dirname = os.path.relpath(dirname, source)
        for f in files:
            dirs.append((os.path.join(basedir, dirname),
                         [os.path.join(source, dirname, f)]))

    dirs.append(('/usr/share/applications', ['pkg/linux/sdls.desktop']))

    return dirs


setup(
    name='sdls',
    version=__version__,
    author='Hoang Chu',
    author_email='hoangbinhc11996@gmail.com',
    description='',

    license='',
    keywords="",
    url='https://github.com/hoangbinhc11996/sdls_project',

    packages=find_packages('src'),
    package_dir={'': 'src'},

    scripts=['sdls'],
    data_files=package_data_dirs('res'),
)
