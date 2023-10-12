import subprocess
import re
import os
import time

from .SensorInterface import SensorInterface

class CPUTemp(SensorInterface):
    def get_data(self) -> list[float]:
        temperature_command = subprocess.run(['vcgencmd', ' measure_temp'], stdout=subprocess.PIPE, text=True)
        temperature_command.check_returncode()
        cpu_temp_str = temperature_command.stdout
        cpu_temp = float(re.search(r'[\d\.]+', cpu_temp_str).group())
        return [cpu_temp]
