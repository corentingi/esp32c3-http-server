from app import network, io, http

try:
    import config
except Exception as e:
    raise "No config file. You can 'cp config.example.py config.py' and edit it"


def run():
    network.connect_wlan()
    io.setup_triggers()
    http.setup_server()
