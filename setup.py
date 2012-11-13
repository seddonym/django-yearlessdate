from distutils.core import setup

setup(
    name = "django-yearlessdate",
    version = "0.1-beta",
    packages = ['djangoyearlessdate'],
    author = "David Seddon",
    author_email = "david@pepperpotdesign.co.uk",
    description = "Django field for storing dates without years",
    url = "http://github.com/seddonym/django-yearlessdate/",
    include_package_data = True
)