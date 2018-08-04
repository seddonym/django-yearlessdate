from django.db import models
from djangoyearlessdate.models import YearlessDateField, YearField
from djangoyearlessdate.helpers import YearlessDate


class YearlessDateModel(models.Model):
    """Sample model for testing YearlessDateField.
    """
    yearless_date = YearlessDateField()
    optional_yearless_date = YearlessDateField(blank=True, null=True)
    yearless_date_with_default = YearlessDateField(default=YearlessDate(day=3, month=5))


class YearModel(models.Model):
    """Sample model for testing YearField.
    """
    year = YearField()
