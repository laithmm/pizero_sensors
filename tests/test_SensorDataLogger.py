import os
import time
import random
import string
import unittest
from unittest.mock import MagicMock

from loggers.SensorDataLogger import SensorDataLogger as SDL
from pizero_sensors.SensorInterface import SensorInterface

SCRIPT_DIR = os.path.dirname(__file__)

class SensorDataLoggerTests(unittest.TestCase):
    def test_givenInitialisation_whenLogFileDoesNotExist_thenAnErrorIsRaised(self):
        with self.assertRaises(FileNotFoundError):
            logger_with_invalid_path = SDL(None, '/tmp/a/path/that/does/not/exist')

    def test_givenInitialisation_whenLogFileExists_thenNoErrorIsRaised(self):
        log_path = Helpers.gen_log_file()
        try:
            SDL(None, log_path)
        except Exception as e:
            raise e

    def test_whenCSVEntryIsGenerated_thenItHasTheCorrectFormat(self):
        sensor = SensorInterface()
        sensor.get_data = MagicMock(return_value=[1.2,3,-4.5])
        log_path = Helpers.gen_log_file()
        logger = SDL(sensor, log_path)
        csv_entry = logger._read_data_and_generate_csv_entry()
        self.assertRegex(csv_entry, '\d+,1\.2,3,-4\.5')

    def test_DataIsWrittenToLogCorrectly(self):
        sensor = SensorInterface()
        sensor.get_data = MagicMock(return_value=[1.2,3,-4.5])
        log_path = Helpers.gen_log_file()
        logger = SDL(sensor, log_path)
        logger.write_data_to_log()
        sensor.get_data = MagicMock(return_value=[3.4,5,-6.7])
        logger.write_data_to_log()
        with open(log_path, 'r') as f:
            log_contents = f.read()
        self.assertRegex(log_contents, '\d+,1\.2,3,-4\.5\n\d+,3\.4,5,-6\.7')

    def test_whenLogDataIsRequested_thenLogsAreReturnedInJSONFormat(self):
        sensor = SensorInterface()
        log_path = f'{SCRIPT_DIR}/../fixtures/sample_dht22.csv'
        logger = SDL(sensor, log_path)
        log_data = logger.return_log_data(1)
        self.assertEqual(len(log_data['data']), 6)

class Helpers:
    def gen_log_file():
        time_of_test = int(time.time())
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        log_path = f'/tmp/sensor-logger-test{time_of_test}{random_string}'
        with open(log_path, 'w+'):
            pass
        return log_path
