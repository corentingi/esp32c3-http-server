"""
TODO:
- Use asyncio to allow running an HTTP server with
    https://docs.micropython.org/en/latest/library/asyncio.html
    https://docs.micropython.org/en/v1.14/library/uasyncio.html
"""
import network

from http_server import MicroPyServer, utils


"""
WLAN SETUP
"""
try:
    from config import NETWORK_SSID, NETWORK_SECRET, NETWORK_STATIC_IP
except:
    NETWORK_SSID = None
    NETWORK_SECRET = None
    NETWORK_STATIC_IP = None

wlan = network.WLAN(network.STA_IF)

def setup_network():
    if NETWORK_STATIC_IP:
        wlan.ifconfig(NETWORK_STATIC_IP)

    if not wlan.isconnected():
        print('Connecting to network %s' % NETWORK_SSID)
        wlan.active(True)
        wlan.connect(NETWORK_SSID, NETWORK_SECRET)

    while True:
        if wlan.isconnected():
            print('Connected')
            break
        print('Waiting for network')
        sleep(1)


"""
HTTP SERVER SETUP
"""
server = MicroPyServer(host="0.0.0.0", port=80)


def hello_world(request):
    utils.send_response(server, "HELLO WORLD!", http_code=200)


def ping(request):
    utils.send_response(server, "PONG", http_code=200)

server.add_route("/", hello_world)
server.add_route("/ping", ping)


"""
MAIN THREAD
"""
if __name__ == "__main__":
    # Setup network
    setup_network()

    # Setup HTTP server
    server.start()
