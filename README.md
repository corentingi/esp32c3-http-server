# HTTP server for MicroPython on ESP32c3

## Usage

Create a `config.py` file to host the network configuration:
```python
NETWORK_SSID = "MyNetworkSSID"
NETWORK_SECRET = "PASSWORD"
NETWORK_STATIC_IP = ('192.168.1.154', '255.255.255.0', '192.168.1.1', '192.168.1.1')
```

Copy the files on your MicroPython device filesystem.
