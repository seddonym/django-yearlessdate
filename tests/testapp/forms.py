from django import forms
from djangoyearlessdate.forms import YearField, YearlessDateField


class YearlessDateForm(forms.Form):
    yearless_date = YearlessDateField()


class YearForm(forms.Form):
    year = YearField()
