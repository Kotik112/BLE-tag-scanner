"""
Script för att styra Philips Hue-lampor

För att köra scriptet behöver du en Hue Bridge och en eller flera Hue-lampor.

Dokumentation för phue-biblioteket:
https://github.com/studioimaginaire/phue/blob/master/README.md

Dokumentation för Converter-biblioteket: (använt för att konvertera färg från RGB till XY)
https://github.com/benknight/hue-python-rgb-converter

TODO: Kolla på create_schedule(), create_group_schedule() och create_scene()

"""

import asyncio
import time
from utils.Bridge import Bridge
from utils.BluetoothScanner import BluetoothScanner

BLE_TAG_MAC = "FF:FF:10:5B:DE:6C"

light_list = []  # Lista av alla lampor

def sort_lights(list):
    """Sortera lamporna i olika grupper baserat på vilket rum de är i"""
    group1 = list[:5]
    group2 = list[5:7]
    group3 = list[7:11]
    group4 = list[11:]

    return group1, group2, group3, group4


def main():
    global light_list
    bridge = Bridge()
    is_found = False
    light_list = bridge.lights
    bed1, bed2, hallway, kitchen = sort_lights(light_list)
    
    while True:
        # Scan for devices
        bt_scanner = BluetoothScanner(BLE_TAG_MAC)
        print("Scanning for devices... (15 seconds)")
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(bt_scanner.run())

        #Check result of scan
        if result:
            if is_found == False:
                print("Change detected: Turning ON Lights!")
                for light in bed1:
                    light.turn_on()
            is_found = True
            # print("DEVICE FOUND")
        else:
            if is_found == True:
                print("Change detected: Turning OFF Lights")
                for light in bed1:
                    light.turn_off()
            is_found = False
            print("DEVICE LOST")

        time.sleep(10)


if __name__ == '__main__':
    main()
