import time
import unittest


class DatabaseInterface:
    def __init__(self):
        # Connecting to database usually takes time.
        # We are simulating it here using sleep.
        time.sleep(2)
        self.records = []
        self.reset_records()

    def reset_records(self):
        self.records = [
            {"title": "Raiders of the Lost Ark", "year": 1981},
            {"title": "Jaws", "year": 1975},
        ]

    def add_record(self, record):
        if (
            not isinstance(record, dict)
            or "title" not in record
            or "year" not in record
        ):
            return False
        self.records.append(record)
        return True

    def get_record(self, idx):
        return self.records[idx]

    def remove_record(self, idx):
        raise NotImplementedError


class TestDatabaseInterface(unittest.TestCase):
    def test_connection_init(self):
        dbi = DatabaseInterface()
        self.assertEqual(len(dbi.records), 2)

    def test_get_record(self):
        dbi = DatabaseInterface()
        dbi.get_record()

    def test_add_record(self):
        dbi = DatabaseInterface()
        seventh_seal = {"title": "Seventh Seal", "year": 1957}
        response = dbi.add_record(seventh_seal)
        self.assertEqual(dbi.records[-1], seventh_seal)
        self.assertTrue(response)

    def test_add_malformed_record(self):
        dbi = DatabaseInterface()
        response = dbi.add_record({"not a good record": 1})
        self.assertFalse(response)

    def test_record_removal(self):
        dbi = DatabaseInterface()
        dbi.remove_record(0)
