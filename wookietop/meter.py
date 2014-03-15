from collections import deque
from datetime import datetime
import platform

import psutil

def available_memory():
    return psutil.virtual_memory()[2]

_readers = {
    'cpu': psutil.cpu_percent,
    'memory': available_memory,
}


class Meter:

    def __init__(self, window=60, reader=None):
        assert callable(reader), 'Meter requires a callable function'

        self.reader = reader
        self.readings = deque(maxlen=window)

    def read(self):
        timestamp = datetime.now()
        reading = self.reader()

        self.add_reading(timestamp, reading)

    def add_reading(self, timestamp, reading):
        self.readings.append((timestamp, reading))


meters = {k: Meter(reader=v) for k,v in _readers.items()}


class SystemInformation:

    @property
    def operating_system(self):
        return {
            'os': platform.system(),
            'version': platform.release(),
            'processor': '64-bit' if platform.processor().endswith('64') else '32-bit',
        }

    @property
    def processor(self):
        return {

        }

    @property
    def memory(self):
        memory = psutil.virtual_memory()
        return {

        }

