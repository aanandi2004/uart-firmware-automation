# UART Firmware Automation

## Project Overview

This project demonstrates UART-based communication between an Arduino UNO and a Python automation framework. The Arduino firmware interfaces with an HC-SR04 ultrasonic sensor, LED, and push button, while the Python application automates testing, data logging, real-time monitoring, and visualization.

The project follows a simple embedded firmware testing workflow where a host PC communicates with the microcontroller through a UART interface using serial commands.

---

## Features

- UART communication using Serial (9600 baud)
- HC-SR04 ultrasonic sensor interfacing
- LED control
- Push button monitoring
- Python UART controller
- Automated UART command testing
- PyTest-based unit testing
- Live serial monitoring
- CSV data logging
- Distance classification (SAFE / WARNING / OUT OF RANGE)
- Distance visualization using Matplotlib
- Modular Python project structure

---

## Hardware Used

- Arduino UNO
- HC-SR04 Ultrasonic Sensor
- LED
- 220 Ω Resistor
- Push Button
- Breadboard
- Jumper Wires
- USB Cable

---

## Software Used

- Arduino IDE
- Python 3
- VS Code
- PySerial
- PyTest
- Matplotlib
- Git
- GitHub

---

## Project Structure

```
uart-firmware-automation
│
├── firmware
│   └── firmware.ino
│
├── python
│   ├── uart_controller.py
│   ├── uart_listener.py
│   ├── uart_test.py
│   ├── test_uart.py
│   └── plot_results.py
│
├── logs
│   ├── live_log.csv
│   └── uart_test_results.csv
│
├── screenshots
│
├── requirements.txt
└── README.md
```

---

## Hardware Connections

| Component | Arduino Pin |
|-----------|-------------|
| HC-SR04 Trig | D13 |
| HC-SR04 Echo | D11 |
| LED | D5 |
| Push Button | D6 |
| VCC | 5V |
| GND | GND |

---

## System Architecture

```
                Python Application
        +-------------------------------+
        | UART Controller               |
        | Live Listener                 |
        | Automated Tests               |
        | CSV Logger                    |
        | Plot Generator                |
        +---------------+---------------+
                        |
                  UART (9600 baud)
                        |
        +---------------+---------------+
        | Arduino UNO                  |
        |                              |
        | HC-SR04 Sensor               |
        | LED                          |
        | Push Button                  |
        +------------------------------+
```

---

## Workflow

1. Upload firmware to Arduino UNO.
2. Connect Arduino through USB.
3. Execute UART automation tests.
4. Log sensor readings into CSV.
5. Monitor live distance measurements.
6. Generate graphs from recorded data.

---

## UART Commands

| Command | Description |
|----------|-------------|
| VERSION | Returns firmware version |
| STATUS | Returns LED, button and distance status |
| LED ON | Turns LED ON |
| LED OFF | Turns LED OFF |

---

## Python Modules

### uart_controller.py

Responsible for UART communication with the Arduino.

### uart_listener.py

Reads live sensor data continuously and stores it in CSV.

### uart_test.py

Runs automated UART command validation.

### test_uart.py

PyTest unit tests.

### plot_results.py

Plots recorded sensor data using Matplotlib.

---

## Sample Output

```
Distance = 19.83 cm | SAFE

Distance = 84.07 cm | WARNING

Distance = 158.43 cm | OUT OF RANGE
```

---

## Test Results

- UART communication verified
- Sensor response verified
- LED control verified
- Button monitoring verified
- Automated command testing passed
- PyTest executed successfully
- Live serial monitoring implemented
- CSV logging implemented
- Graph generation implemented

---

## Results

- UART communication established successfully.
- Automated testing framework achieved 100% test pass rate.
- Real-time sensor monitoring implemented.
- Distance data successfully logged and visualized.
- Modular project organization for firmware and software components.

---

## Future Improvements

- Rewrite firmware using Bare-Metal C (ATmega328P Registers)
- Interrupt-driven UART communication
- Timer-based ultrasonic measurement
- CRC-based UART packet validation
- Non-blocking firmware architecture
- GitHub Actions CI/CD
- Hardware-in-the-loop (HIL) testing
- FreeRTOS implementation

---

## Technologies

- Embedded C
- Arduino
- UART
- Python
- PySerial
- PyTest
- CSV
- Matplotlib
- Git
- GitHub

---

## Author

**Aanandi Aarya**

Electronics and Communication Engineering

Embedded Systems | Firmware Development | VLSI