from djangoyearlessdate.helpers import YearlessDate
from djangoyearlessdate.forms import YearlessDateSelect
from .testapp.forms import YearForm, YearlessDateForm


class TestYearlessDateWidget:
    def test_decompress_with_value(self):
        assert YearlessDateSelect().decompress(YearlessDate(22, 6)) == [22, 6]

    def test_decompress_without_value(self):
        assert YearlessDateSelect().decompress(None) == [None, None]


class TestYearlessDateField:
    def test_valid_yearless_date(self):
        form = YearlessDateForm(data={'yearless_date_0': '1', 'yearless_date_1': '9'})
        assert form.is_valid()
        assert form.cleaned_data['yearless_date'] == YearlessDate(1, 9)

    def test_invalid_yearless_date(self):
        form = YearlessDateForm(data={'yearless_date_0': '31', 'yearless_date_1': '9'})
        assert not form.is_valid()
        assert form.errors['yearless_date'] == [u'Invalid date.']

    def test_yearless_date_not_supplied(self):
        form = YearlessDateForm(data={'yearless_date_0': '', 'yearless_date_1': ''})
        assert not form.is_valid()
        assert form.errors['yearless_date'] == [u'This field is required.']


class TestYearField:
    def test_1900_is_valid(self):
        form = YearForm(data={'year': '1900'})
        assert form.is_valid()
        assert form.cleaned_data['year'] == 1900

    def test_2200_is_valid(self):
        form = YearForm(data={'year': '2200'})
        assert form.is_valid()
        assert form.cleaned_data['year'] == 2200

    def test_pre_1900_year_is_invalid(self):
        form = YearForm(data={'year': '1899'})
        assert not form.is_valid()
        assert form.errors['year'] == [u'Invalid year.']

    def test_post_2200_year_is_invalid(self):
        form = YearForm(data={'year': '2201'})
        assert not form.is_valid()
        assert form.errors['year'] == [u'Invalid year.']
