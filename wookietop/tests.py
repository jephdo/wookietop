import unittest
from .meter import Meter


class TestMeter(unittest.TestCase):
    def setUp(self):
        self.meter = Meter()

        def reader():
            return 1

        self.dummy_reader = reader
    def test_meter_requires_callable_reader(self):
        pass

    def test_add_reading(self):
        meter = Meter(reader=self.dummy_reader)

        for _ in range(3):
            timestamp = datetime.now()
            reading = self.dummy_reader()
            meter.add_reading(timestamp, reading)
            self.assertEqual(self.readings[-1], (timestamp, reading))

    def test_readings_dont_exceed_maxlen(self):
        max_len = 5

        meter = Meter(window=max_len, reader=self.dummy_reader)

        for _ in range(max_len):
            meter.read()

        meter.read()

        self.assertEqual(len(meter.readings), max_len)







