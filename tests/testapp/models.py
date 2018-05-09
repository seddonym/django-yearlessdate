from django.db import models
from djangoyearlessdate.models import YearlessDateField, YearField


class YearlessDateModel(models.Model):
    """Sample model for testing YearlessDateField.
    """
    yearless_date = YearlessDateField()


class YearModel(models.Model):
    """Sample model for testing YearField.
    """
    year = YearField()
