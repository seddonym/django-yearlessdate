from django.db import models
from helpers import YearlessDate
import forms

class YearlessDateField(models.Field):
    "A model field for storing dates without years"
    description = "A date without a year, for use in things like birthdays"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 4
        super(YearlessDateField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if isinstance(value, YearlessDate):
            return value
        if not value:
            return None
        # The string case.
        return YearlessDate(value[2:], value[:2])

    def from_db_value(self, value, expression, connection, context):
        if not value:
            return None
        # The string case.
        return YearlessDate(value[2:], value[:2])

    
    def get_prep_value(self, value):
        "The reverse of to_python, for inserting into the database"
        if value is not None:
            return ''.join(["%02d" % i for i in (value.month, value.day)])
    
    def get_internal_type(self):
        return 'CharField'
    
    def value_to_string(self, obj):
        "For serialization"
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)
    
    def formfield(self, **kwargs):
        # This is a fairly standard way to set up some defaults
        # while letting the caller override them.
        defaults = {'form_class': forms.YearlessDateField}
        defaults.update(kwargs)
        return super(YearlessDateField, self).formfield(**defaults)
    
class YearField(models.IntegerField):
    "A model field for storing years, e.g. 2012"
    def formfield(self, **kwargs):
        defaults = {'form_class': forms.YearField}
        defaults.update(kwargs)
        return super(YearField, self).formfield(**defaults)
    
#South integration
try:
    from south.modelsinspector import add_introspection_rules
except ImportError:
    #South is not installed
    pass
else:
    add_introspection_rules([], ["^djangoyearlessdate\.models\.YearlessDateField"])
    add_introspection_rules([], ["^djangoyearlessdate\.models\.YearField"])