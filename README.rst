django-yearlessdate
===================

Provides a Django model and form fields for dates that do not require years.

One use case is to collect birthdays without requiring the year of birth.

Prerequisites
--------------------

- Django 1.8 - 1.10
- Python 2.7

(Other versions may be supported, but are untested.)

Installation
--------------------

    pip install django-yearlessdate

Usage
--------------------

The package provides two model fields, YearlessDateField and YearField.

YearlessDateField provides dropdowns for day and month, and will validate
accordingly.  For example, a user won't be able to set the date to April 31st.
The YearField is a very simple field that just ensures the year provided lies between
1900 and 2200.  (This range will become user configurable at some point.) 

Here's an example models.py that declares a model with a required yearless date
and an optional year::  

    from django.db import models
    from djangoyearlessdate.models import YearlessDateField, YearField
  
    class MyModel(models.Model):
        birthday = YearlessDateField()
        year = YearField(null=True, blank=True)

The values of YearlessDateField on the model instances can be accessed like so:

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

Tests
---------------------------

Setup:

1. Ensure you have a recent version of tox installed.
2. Clone this repo.

Running tests:

From the root of this repo, run:

    tox

