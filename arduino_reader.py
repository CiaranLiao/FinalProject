# arduino_reader.py
import serial
import threading

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
sensor_data = {"sound": 0, "pressure": 0}

def read_sensors():
    while True:
        data = arduino.readline().decode('utf-8').rstrip()
        if data:
            try:
                sound_value, pressure_value = map(int, data.split(','))
                sensor_data["sound"] = sound_value/10.0
                sensor_data["pressure"] = pressure_value/50.0

            except ValueError:
                pass

# 线程
sensor_thread = threading.Thread(target=read_sensors, daemon=True)
sensor_thread.start()

def get_sensor_data():
    return sensor_data