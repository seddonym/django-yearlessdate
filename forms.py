from django import forms
from django.forms.widgets import MultiWidget, TextInput
from django.core.validators import ValidationError
from django.forms.widgets import Select
from django.utils.encoding import force_unicode
from django.utils.html import escape, conditional_escape
from django.forms.util import flatatt

import calendar
from helpers import DateInYear

DAY_CHOICES =  tuple([('','---------' )] + [(i,i) for i in range(1,32)])
MONTH_CHOICES = tuple([('','---------' )] + [(i, calendar.month_name[i]) for i in range(1,13)])

    
class DateInYearSelect(MultiWidget):
    def __init__(self, *args, **kwargs):
        widgets = (Select(attrs={'class': 'select-dateinyear-day'}, choices=DAY_CHOICES), Select(attrs={'class': 'select-dateinyear-month'}, choices=MONTH_CHOICES))
        super(DateInYearSelect, self).__init__(widgets=widgets, *args, **kwargs)

    def decompress(self, value):
        if value is None:
            return [None,None]
        return [value.day, value.month]
   
class DateInYearField(forms.Field):
    widget = DateInYearSelect
    
    def clean(self, value):
        if value == ['','']:
            #If the values are both None, trigger the default validation for null
            super(DateInYearField, self).clean(None)
        else:
            try:
                return DateInYear(*value)
            except:
                raise ValidationError('Invalid date.')
        

class YearField(forms.Field):
    widget = TextInput
    
    def clean(self, value):
        #First, run general validation (will catch, for example, a blank entry
        #if the field is required
        super(YearField, self).clean(value)
        
        try:
            value = int(value)
            #TODO: allow customization of these limits
            if value < 1900 or value > 2200:
                raise Exception()
            return value
        except:
            raise ValidationError('Invalid year.')
        