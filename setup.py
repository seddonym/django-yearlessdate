import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages
setup(
    name = "django-yearlessdate",
    version = "0.1",
    packages = find_packages(),
    author = "David Seddon",
    author_email = "david@pepperpotdesign.co.uk",
    description = "Django field for storing dates without years",
    url = "http://github.com/seddonym/django-yearlessdate/",
    include_package_data = True
)