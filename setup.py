import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django_http_api",
    version="0.1.0",
    packages=["django_http_api"],
    package_data = {
        'django_http_api': ['py.typed'],
    },
    include_package_data=True,
    license="MIT License",
    description="A Django app to build an HTTP API without hassle",
    long_description=README,
    url="https://github.com/nmtitov/django-http-api",
    author="Nikita Titov",
    author_email="nik@titov.dev",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
