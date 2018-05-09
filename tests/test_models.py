import pytest
from djangoyearlessdate.helpers import YearlessDate
from djangoyearlessdate import forms
from .testapp.models import YearlessDateModel, YearModel
from .testapp.formfields import MyCustomFormField

pytestmark = pytest.mark.django_db


class TestYearlessDateField:
    def test_storage_and_retrieval(self):
        yearless_date = YearlessDate(3, 7)
        model = YearlessDateModel(yearless_date=yearless_date)
        model.save()
        retrieved_model = YearlessDateModel.objects.get(id=model.id)
        assert retrieved_model.yearless_date == yearless_date

    def test_empty_values(self):
        model = YearlessDateModel()
        assert model.yearless_date == None

    def test_value_to_string(self):
        yearless_date = YearlessDate(3, 7)
        model = YearlessDateModel(yearless_date=yearless_date)
        field = model._meta.get_field('yearless_date')
        assert field.value_to_string(model) == '0703'

    def test_form_field_default(self):
        model = YearlessDateModel(yearless_date=YearlessDate(1, 9))
        field = model._meta.get_field('yearless_date')
        assert isinstance(field.formfield(), forms.YearlessDateField)

    def test_form_field_can_be_overridden(self):
        model = YearlessDateModel(yearless_date=YearlessDate(1, 9))
        field = model._meta.get_field('yearless_date')
        assert isinstance(
            field.formfield(form_class=MyCustomFormField),
            MyCustomFormField
        )

    def test_ordering(self):
        # Create some instances, not in date order
        sep_1 = YearlessDateModel.objects.create(yearless_date=YearlessDate(1, 9))
        nov_10 = YearlessDateModel.objects.create(yearless_date=YearlessDate(10, 11))
        jan_29 = YearlessDateModel.objects.create(yearless_date=YearlessDate(29, 1))
        jan_9 = YearlessDateModel.objects.create(yearless_date=YearlessDate(9, 1))
        aug_5 = YearlessDateModel.objects.create(yearless_date=YearlessDate(5, 8))

        model_ids_in_order = [jan_9.id, jan_29.id, aug_5.id, sep_1.id, nov_10.id]

        # Pull the models from the database, ordering by date
        retrieved_models = YearlessDateModel.objects.filter(
            id__in=model_ids_in_order
        ).order_by('yearless_date').values_list('id', flat=True)

        # Check the lists are the same
        assert all([a == b for a, b in zip(retrieved_models, model_ids_in_order)])


class TestYearFieldModel:
    def test_form_field_default(self):
        model = YearModel(year=1950)
        field = model._meta.get_field('year')
        assert isinstance(field.formfield(), forms.YearField)

    def test_form_field_can_be_overridden(self):
        model = YearModel(year=1950)
        field = model._meta.get_field('year')
        assert isinstance(
            field.formfield(form_class=MyCustomFormField),
            MyCustomFormField
        )
