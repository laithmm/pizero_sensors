import time
import adafruit_dht
from board import D4

from .SensorInterface import SensorInterface

class DHT22(SensorInterface):
    """implements SensorInterface"""

    def get_data(self) -> list[float]:
        """overrides SensorInterface.get_data()"""
        temperature = None
        humidity = None
    
        while temperature == None or humidity == None:
            self.device = adafruit_dht.DHT22(D4)
            try:
                temperature = self.device.temperature
                humidity = self.device.humidity
                print('Data read successfully', temperature, humidity)
                self.device.exit()
                return [temperature, humidity]
            except RuntimeError as error:
                self.device.exit()

                if 'sensor not found' in error.args[0]:
                    raise error

                print(f'error reading from DHT22: {error.args[0]}')
                time.sleep(2.0)
                continue
            except Exception as error:
                self.device.exit()
                raise error


if __name__ == '__main__':
    DHT22().get_data()
