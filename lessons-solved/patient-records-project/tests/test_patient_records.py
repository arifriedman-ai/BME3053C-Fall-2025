import unittest
from src.patient_records import PatientRecords

class TestPatientRecords(unittest.TestCase):

    def setUp(self):
        self.records = PatientRecords()

    def test_add_record(self):
        self.records.add_record("John Doe", 30, "A+")
        self.assertEqual(len(self.records.get_all_records()), 1)
        self.assertEqual(self.records.get_all_records()[0]['name'], "John Doe")

    def test_update_record(self):
        self.records.add_record("Jane Doe", 25, "B+")
        self.records.update_record("Jane Doe", age=26)
        self.assertEqual(self.records.get_all_records()[0]['age'], 26)

    def test_retrieve_record(self):
        self.records.add_record("Alice Smith", 28, "O-")
        record = self.records.get_record("Alice Smith")
        self.assertIsNotNone(record)
        self.assertEqual(record['name'], "Alice Smith")

    def test_invalid_age(self):
        with self.assertRaises(ValueError):
            self.records.add_record("Invalid Age", -1, "B+")

    def test_basic_statistical_analysis(self):
        self.records.add_record("Patient 1", 30, "A+")
        self.records.add_record("Patient 2", 40, "B+")
        self.records.add_record("Patient 3", 50, "O-")
        average_age = self.records.get_average_age()
        self.assertEqual(average_age, 40)

if __name__ == '__main__':
    unittest.main()