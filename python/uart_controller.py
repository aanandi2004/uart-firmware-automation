#simple command to send and receive data from the arduino using uart serial communication
#port open and then closed everytime a command is sent and received
'''import serial
import time

arduino = serial.Serial('/dev/cu.usbserial-A5069RR4', 9600, timeout=2)
time.sleep(2)

print("After opening:", arduino.is_open)

def send_command(command):
    print("Before write:", arduino.is_open)

    formatted_command = f"{command.strip()}\n"

    arduino.write(formatted_command.encode())
    arduino.flush()

    response = arduino.read_until(b'\n').decode().strip()
    return response

def close_connection():
    print("Closing port")
    arduino.close()'''


import serial
import time

arduino = serial.Serial('/dev/cu.usbserial-A5069RR4', 9600, timeout=2)
time.sleep(2)

print("Connected to Arduino")

def read_distance():
    response = arduino.readline().decode().strip()
    return response

def close_connection():
    arduino.close()