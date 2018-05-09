from unittest import TestCase
from djangoyearlessdate.helpers import YearlessDate


class TestYearlessDateDisplay(TestCase):
    def test_str(self):
        self.assertEqual(
            str(YearlessDate(15, 6)),
            '15 June'
        )

    def test_month_name(self):
        self.assertEqual(
            YearlessDate(30, 12).month_name, 'December'
        )


class TestYearlessDateValidity(TestCase):
    def test_invalid_month_raises_exception(self):
        with self.assertRaisesRegexp(
                Exception,
                'Cannot create DateInYear object with a month value of 0.'):
            YearlessDate(1, 0)

    def test_invalid_day_raises_exception(self):
        # February never has 30 days
        with self.assertRaisesRegexp(
                Exception,
                'Cannot create DateInYear object - invalid day value 30 for month February.'):
            YearlessDate(30, 2)

    def test_leap_year_date_is_valid(self):
        yearless_date = YearlessDate(29, 2)
        self.assertEqual(yearless_date.day, 29)
        self.assertEqual(yearless_date.month, 2)


class TestYearlessDateEquality(TestCase):
    def assert_equal_thorough(self, a, b):
        """Assert that a equals b.
        For thoroughness, also tests that a != b is not true, as the implementations
        of equality and inequality are separate.
        """
        self.assertTrue(a == b)
        self.assertFalse(a != b)

    def assert_not_equal_thorough(self, a, b):
        """Assert that a does not equal b.
        For thoroughness, also tests that a == b is false, as the implementations
        of equality and inequality are separate.
        """
        self.assertFalse(a == b)
        self.assertTrue(a != b)
        
    def test_identical_dates_are_equal(self):
        self.assert_equal_thorough(
            YearlessDate(15, 6),
            YearlessDate(15, 6)
        )

    def test_same_day_different_months_are_not_equal(self):
        self.assert_not_equal_thorough(
            YearlessDate(15, 3),
            YearlessDate(15, 6)
        )

    def test_different_days_same_month_are_not_equal(self):
        self.assert_not_equal_thorough(
            YearlessDate(12, 6),
            YearlessDate(15, 6)
        )

    def test_non_yearless_dates_are_not_equal(self):
        self.assert_not_equal_thorough(
            YearlessDate(9, 6),
            'foo'
        )


class TestYearlessDateGreaterThan(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.earlier = YearlessDate(30, 9)
        cls.later = YearlessDate(1, 10)

    def test_later_date_is_greater_than_earlier_date(self):
        self.assertTrue(
            self.later > self.earlier
        )

    def test_earlier_date_is_not_greater_than_later_date(self):
        self.assertFalse(
            self.earlier > self.later
        )

    def test_equal_dates_are_not_greater_than(self):
        self.assertFalse(
            YearlessDate(30, 9) >  YearlessDate(30, 9)
        )


class TestYearlessDateGreaterThanOrEqual(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.earlier = YearlessDate(30, 9)
        cls.later = YearlessDate(1, 10)

    def test_later_date_is_greater_than_or_equal_to_earlier_date(self):
        self.assertTrue(
            self.later >= self.earlier
        )

    def test_earlier_date_is_not_greater_than_or_equal_to_later_date(self):
        self.assertFalse(
            self.earlier >= self.later
        )

    def test_equal_dates_are_greater_than_or_equal_to(self):
        self.assertTrue(
            YearlessDate(30, 9) >= YearlessDate(30, 9)
        )


class TestYearlessDateLessThan(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.earlier = YearlessDate(30, 9)
        cls.later = YearlessDate(1, 10)

    def test_earlier_date_is_less_than_later_date(self):
        self.assertTrue(
            self.earlier < self.later
        )

    def test_later_date_is_not_less_than_earlier_date(self):
        self.assertFalse(
            self.later < self.earlier
        )

    def test_equal_dates_are_not_less_than(self):
        self.assertFalse(
            YearlessDate(30, 9) < YearlessDate(30, 9)
        )


class TestYearlessDateLessThanOrEqual(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.earlier = YearlessDate(30, 9)
        cls.later = YearlessDate(1, 10)

    def test_earlier_date_is_less_than_or_equal_to_later_date(self):
        self.assertTrue(
            self.earlier <= self.later
        )

    def test_earlier_date_is_not_less_than_or_equal_to_later_date(self):
        self.assertFalse(
            self.later <= self.earlier
        )

    def test_equal_dates_are_less_than_or_equal_to(self):
        self.assertTrue(
            YearlessDate(30, 9) <= YearlessDate(30, 9)
        )
