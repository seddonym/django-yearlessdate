from setuptools import setup
import codecs

long_description = codecs.open('README.rst', 'r', 'utf-8').read()

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Framework :: Django',
    'Framework :: Django :: 1.8',
    'Framework :: Django :: 1.9',
    'Framework :: Django :: 1.10',
    'Framework :: Django :: 1.11',
    'Operating System :: OS Independent',
]

setup(
    name="django-yearlessdate",
    version="1.0.1",
    packages=['djangoyearlessdate'],
    author="David Seddon",
    author_email="david@seddonym.me",
    description="Django field for storing dates without years.",
    long_description=long_description,
    keywords='django date yearlessdate',
    url="http://github.com/seddonym/django-yearlessdate/",
    platforms=['any'],
    license='BSD',
    classifiers=classifiers,
)
