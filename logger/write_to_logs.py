import sys, time

from pizero_sensors.DHT22 import DHT22
from pizero_sensors.CPUTemp import CPUTemp

LOGS_DIR = None

def write_to_dht22_log():
    temperature, humidity = DHT22().get_data()

    logfile = f'{LOGS_DIR}/dht22.log'
    print(f'writing to dht22 log ({logfile}): temp {temperature}, humidity {humidity}')
    with open(logfile, 'a') as log:
        log.write(f'{round(time.time())},{temperature},{humidity}\n')

def write_to_cpu_temp_log():
    cpu_temp, = CPUTemp().get_data()

    logfile = f'{LOGS_DIR}/cpu-temp.log'
    print(f'writing cpu temp to log ({logfile}): {cpu_temp}')
    with open(logfile, 'a') as log:
        log.write(f'{round(time.time())},{cpu_temp}\n')

if __name__=='__main__':
    LOGS_DIR = sys.argv[1]
    write_to_dht22_log()
    write_to_cpu_temp_log()
