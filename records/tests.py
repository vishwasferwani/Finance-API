from django.test import TestCase
from .serializers import RecordSerializer
# Create your tests here.


class RecordUnitTest(TestCase):
    #unit test for validating negative amount
    def test_negative_amount(self):
        data = {
            "amount": -100,
            "type": "expense",
            "category": "Food",
            "date": "2026-04-02"
        }

        serializer = RecordSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn('amount', serializer.errors)
    
    #type not provided
    def test_missing_record(self):
        data = {
            "amount": 100,
            "category": "Salary",
            "date": "2026-04-02"
        }

        serializer = RecordSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('type', serializer.errors)