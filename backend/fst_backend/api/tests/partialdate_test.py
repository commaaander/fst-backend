from django.core.exceptions import ValidationError
from django.test import TestCase
import logging

from fst_backend.api.fields import PartialDate, PartialDateField
from fst_backend.api.models import Person

logger = logging.getLogger(__name__)


class PartialDateTestCase(TestCase):
    def test_valid_dates(self):
        # Test fully specified date
        full_date = PartialDate("2023-11-06")
        self.assertEqual(full_date.year, 2023)
        self.assertEqual(full_date.month, 11)
        self.assertEqual(full_date.day, 6)

        # Test year-month format
        year_month = PartialDate("2022-01")
        self.assertEqual(year_month.year, 2022)
        self.assertEqual(year_month.month, 1)
        self.assertEqual(year_month.day, 0)

        # Test month-day format
        month_day = PartialDate("11-06")
        self.assertEqual(month_day.year, 0)
        self.assertEqual(month_day.month, 11)
        self.assertEqual(month_day.day, 6)

        empty_date = PartialDate("")
        self.assertEqual(empty_date.year, 0)
        self.assertEqual(empty_date.month, 0)
        self.assertEqual(empty_date.day, 0)

        none_date = PartialDate(None)
        self.assertEqual(none_date.year, 0)
        self.assertEqual(none_date.month, 0)
        self.assertEqual(none_date.day, 0)

    def test_invalid_dates(self):
        with self.assertRaises(ValueError):
            PartialDate("2023-13-01")  # Test invalid date format
            PartialDate("2023-02-30")  # Test non-existing date
            PartialDate("13-32")  # Test invalid month-day format

    def test_string_representation(self):
        # Test string representation with zero padding
        date = PartialDate("2023-11-6")
        self.assertEqual(str(date), "2023-11-06")


class PartialDateFieldTestCase(TestCase):
    def test_partial_date_field_from_db(self):
        # Assuming you have a model with a PartialDateField called MyModel
        model_instance = Person.objects.create(lastname="Mustermann", birthday="2023-11-06")
        model_instance.refresh_from_db()

        self.assertIsInstance(model_instance.birthday, PartialDate)
        self.assertEqual(model_instance.birthday.year, 2023)
        self.assertEqual(model_instance.birthday.month, 11)
        self.assertEqual(model_instance.birthday.day, 6)

    def test_partial_date_field_to_python(self):
        # Ensure to_python is converting to PartialDate object
        partial_date_field = PartialDateField()
        result = partial_date_field.to_python("2023-11-06")

        self.assertIsInstance(result, PartialDate)
        self.assertEqual(result.year, 2023)
        self.assertEqual(result.month, 11)
        self.assertEqual(result.day, 6)

    def test_valid_dates(self):
        model_instance = Person.objects.create(lastname="Mustermann", birthday="2023-11-06")
        model_instance.refresh_from_db()
        self.assertEqual(model_instance.birthday.year, 2023)
        self.assertEqual(model_instance.birthday.month, 11)
        self.assertEqual(model_instance.birthday.day, 6)

        model_instance = Person.objects.create(lastname="Mustermann", birthday="2023")
        model_instance.refresh_from_db()
        self.assertEqual(model_instance.birthday.year, 2023)
        self.assertEqual(model_instance.birthday.month, 0)
        self.assertEqual(model_instance.birthday.day, 0)

        model_instance = Person.objects.create(lastname="Mustermann", birthday="2023-11")
        model_instance.refresh_from_db()
        self.assertEqual(model_instance.birthday.year, 2023)
        self.assertEqual(model_instance.birthday.month, 11)
        self.assertEqual(model_instance.birthday.day, 0)

        model_instance = Person.objects.create(lastname="Mustermann", birthday="11")
        model_instance.refresh_from_db()
        self.assertEqual(model_instance.birthday.year, 0)
        self.assertEqual(model_instance.birthday.month, 11)
        self.assertEqual(model_instance.birthday.day, 0)

        model_instance = Person.objects.create(lastname="Mustermann", birthday="11-06")
        model_instance.refresh_from_db()
        self.assertEqual(model_instance.birthday.year, 0)
        self.assertEqual(model_instance.birthday.month, 11)
        self.assertEqual(model_instance.birthday.day, 6)

        model_instance = Person.objects.create(lastname="Mustermann", birthday="")
        model_instance.refresh_from_db()
        self.assertEqual(model_instance.birthday.year, 0)
        self.assertEqual(model_instance.birthday.month, 0)
        self.assertEqual(model_instance.birthday.day, 0)

    def test_invalid_dates(self):
        invalid_dates = ["2023-02-30", "02-30", "2023-02-30", "2023-15-30", "2023-12-50", "invalid-date"]

        for invalid_date in invalid_dates:
            p = Person.objects.create(lastname="Mustermann", birthday=invalid_date)
            self.assertRaises(ValidationError, p.refresh_from_db)
