===================
django-yearlessdate
===================

Provides a Django model and form fields for dates that do not include years.

One use case is to collect birthdays without requiring the year of birth.

|build-status| |python-versions| |django-versions| |wheel| |license|

Prerequisites
=============

- Django 1.8 - 1.11, 2.0
- Python 2.7, 3.6

(Other versions may function, but are untested.)

Installation
============

.. code-block:: console

    pip install django-yearlessdate

Usage
=====

The package provides two model fields, ``YearlessDateField`` and ``YearField``.

YearlessDateField
-----------------

``YearlessDateField`` stores a date without a year: January 1st, for example.

Its default widget consists of two dropdowns, one for a day and one for the month.

It will only allow potentially valid dates. For example, a user won't be able to set
the date to April 31st. February 29th is counted as a valid date.

Here's an example ``models.py`` that declares a model with a required yearless date::

    from django.db import models
    from djangoyearlessdate.models import YearlessDateField
  
    class MyModel(models.Model):
        birthday = YearlessDateField()

The values of ``YearlessDateField`` on the model instances can be accessed like so:

>>> a = MyModel.objects.get(id=1)
>>> a
<MyModel: 4 August 2011>
>>> a.birthday.day
4
>>> a.birthday.month
8
>>> print a.birthday
4 August

They can also be compared or sorted as would be expected, for example:

>>> m = MyModel.objects.all() 
>>> m
[<MyModel: 4 August 2011>, <MyModel: 30 June 2013>]
>>> m[0].birthday > m[1].birthday
True
>>> m.order_by('birthday')
[<MyModel: 30 June 2013>, <MyModel: 4 August 2011>]

YearField
---------

``YearField`` is a very simple model field that stores the year as an integer,
and ensures the year provided lies between 1900 and 2200::

    from django.db import models
    from djangoyearlessdate.models import YearField

    class MyModel(models.Model):
        year = YearField(null=True, blank=True)

Use of ``YearField`` is *not recommended* due to its lack of configurability.
You're almost certainly better of using a ``SmallIntegerField`` in combination
with a ``MinValueValidator`` and a ``MaxValueValidator``.

Running tests
=============

Setup
-----

1. Ensure you have a recent version of tox installed.
2. Clone this repo.

Running tests
-------------

From the root of this repo, simply run:

.. code-block:: console

    tox

.. |build-status| image:: https://img.shields.io/circleci/project/github/seddonym/django-yearlessdate/master.svg
    :alt: Build status
    :target: https://circleci.com/gh/seddonym/django-yearlessdate

.. |python-versions| image:: https://img.shields.io/pypi/pyversions/django-yearlessdate.svg
    :alt: Python versions
    :target: http://pypi.python.org/pypi/django-yearlessdate/

.. |django-versions| image:: https://img.shields.io/pypi/djversions/django-yearlessdate.svg
    :alt: Django compatibility
    :target: http://pypi.python.org/pypi/django-yearlessdate/

.. |wheel| image:: https://img.shields.io/pypi/wheel/django-yearlessdate.svg
    :alt: django-yearlessdate can be installed via wheel
    :target: http://pypi.python.org/pypi/django-yearlessdate/

.. |license| image:: https://img.shields.io/pypi/l/django-yearlessdate.svg
    :alt: django-yearlessdate can be installed via wheel
    :target: http://pypi.python.org/pypi/django-yearlessdate/
