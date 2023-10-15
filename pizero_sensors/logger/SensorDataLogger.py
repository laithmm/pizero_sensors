import time
from datetime import datetime
from .helpers.csv_helpers import *

class SensorDataLogger:
    def __init__(self, sensor, log_path):
        try:
            with open(log_path, 'r'):
                pass
        except Exception as e:
            raise e

        self.sensor = sensor
        self.log_path = log_path

    def write_data_to_log(self):
        with open(self.log_path, 'a') as logfile:
            logfile.write(f'{self._read_data_and_generate_csv_entry()}\n')

    def return_log_data(self, hours, minutes=0, human_readable=False):
        logs_array = read_csv_into_nested_list(self.log_path)
        headings = logs_array[0]
        log_data = logs_array[1:]

        seconds = (hours * 60**2) + (minutes * 60)
        most_recent_log_time = log_data[-1][0]

        num_data_points_to_return = 0
        for entry in log_data[::-1]:
            if entry[0] <= most_recent_log_time - seconds:
                break
            num_data_points_to_return += 1
            
        to_return = log_data[::-1][:num_data_points_to_return]
        if human_readable:
            for i, _ in enumerate(to_return):
                to_return[i][0] = datetime.utcfromtimestamp(to_return[i][0]).strftime('%H:%M:%S %d-%m-%Y')

        return {'headings': headings, 'data': to_return}


    def _read_data_and_generate_csv_entry(self):
        data = self.sensor.get_data()
        csv_entry = f'{round(time.time())}'
        for d in data:
            csv_entry += f',{d}'
        return csv_entry
