# To build and upload a new version, follow the steps below.
# Notes:
# - this is a "Universal Wheels" package that is pure Python and supports both Python2 and Python3
# - Twine is a secure PyPi upload package
# - Make sure you have bumped the version! at ts/version.py
# $ pip install twine
# $ pip install wheel
# $ python setup.py bdist_wheel --universal

# *** TEST YOUR PACKAGE WITH TEST PI ******
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# If this is successful then push it to actual pypi

# $ twine upload dist/*
"""
Setup.py for the expath package
"""

import io
import re
import os
from os import path
from setuptools import find_packages, setup


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'readme.md'), encoding='utf-8') as readme_file:
    long_description = readme_file.read()

VERSION = find_version('expath', '__init__.py')


if __name__ == '__main__':
    setup(
        name='expath',
        version = VERSION,

        include_package_data=True,

        description='Path lib extends from the pathlib',
        long_description=long_description,
        long_description_content_type="text/markdown",

        # Author details
        author='csJoax',
        author_email='joax@qq.com',
        url='https://github.com/csJoax/expath.git',

        # Package info
        packages=find_packages(exclude=('test',)),

        python_requires='>=3',
        license='MIT',
        zip_safe=True,
        keywords='Extend Path Lib',

        classifiers=[
            'Operating System :: OS Independent',
            'License :: OSI Approved :: BSD License',
            'Natural Language :: English',
            # Supported python versions
            'Programming Language :: Python :: 3',
        ],
    )
