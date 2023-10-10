import time
import adafruit_dht
from board import D4

from sensors.SensorInterface import SensorInterface

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
                # Errors happen fairly often, DHT's are hard to read, just keep going
                print(error.args[0])
                self.device.exit()
                time.sleep(2.0)
                continue
            except Exception as error:
                self.device.exit()
                raise error


if __name__ == '__main__':
    DHT22().get_data()
