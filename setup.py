import sys
from setuptools import find_packages, setup

TITLE = "tocamelcase"
VERSION = "0.0.4"
SUMMARY = "🐫 To Camel Case: self explanatory!"
LIC = "MIT"

AUTHOR_NAME = "Carlos Abraham"
AUTHOR_MAIL = "abraham@abranhe.com"

__license__ = "MIT"
__copyright__ = "Copyright 2018 Carlos Abraham"


def open_file(filename):
    """Open and read the file *filename*."""
    with open(filename) as f:
        return f.read()

setup(
    name=TITLE,
    packages = ["tocamelcase"],
    version=VERSION,
    description=SUMMARY,
    author=AUTHOR_NAME,
    author_email=AUTHOR_MAIL,
    include_package_data=True,
    project_urls={
        'Source': 'https://github.com/abranhe/tocamelcase/',
    },
    license=LIC,
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
