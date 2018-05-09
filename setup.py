from setuptools import setup
import codecs

long_description = codecs.open('README.rst', 'r', 'utf-8').read()

setup(
    name="django-yearlessdate",
    version="1.0",
    packages=['djangoyearlessdate'],
    author="David Seddon",
    author_email="david@seddonym.me",
    description="Django field for storing dates without years.",
    long_description=long_description,
    url="http://github.com/seddonym/django-yearlessdate/",

)
