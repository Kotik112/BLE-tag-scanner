# BLE-tag-scanner
This program scans for a specific BLE (Bluetooth Low Energy) tag using its MAC address, and controls a set of lights based on whether the tag is found. The lights can be grouped and controlled separately.

# Getting Started
Make sure you have Python 3.7 or later installed on your system.
### Install the required dependencies by running:
- pip install phue
- pip install bleak
Replace BLE_TAG_MAC with the MAC address of your BLE tag.
Run the program with python main.py.
Functionality
The program uses the BluetoothScanner class to scan for the BLE tag with the specified MAC address.
If the tag is found, the program turns on the lights in the bed1 group. If the tag is not found, the lights are turned off.
The lights can be grouped and sorted using the sort_lights function.
The program runs the scan every 10 seconds and prints the result to the console.
Dependencies
asyncio
time
utils.Bridge
utils.BluetoothScanner
Limitations
The program currently only supports controlling lights in the bed1 group and does not support multiple groups.
The program currently only supports turning lights on or off and does not support adjusting brightness or color.
The program currently only supports scanning every 10 seconds and does not support configurable intervals.
Additional notes
The Bridge class is used to connect and steer the lights.
The program uses the asyncio library to run the scanning process in the background.
