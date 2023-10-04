from time import sleep

import network
import config


def connect_wlan():
    wlan = network.WLAN(network.STA_IF)

    if config.NETWORK_STATIC_IP:
        wlan.ifconfig(config.NETWORK_STATIC_IP)

    if not wlan.isconnected():
        print(f'Connecting to network {config.NETWORK_SSID}')
        wlan.active(True)
        wlan.connect(config.NETWORK_SSID, config.NETWORK_SECRET)

    while True:
        if wlan.isconnected():
            print('Connected')
            return

        print('Waiting for network...')
        sleep(1)
