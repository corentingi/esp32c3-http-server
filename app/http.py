import config
from app import io

def setup_server():
    from micropyserver import MicroPyServer, utils

    server = MicroPyServer(host="0.0.0.0", port=80)

    def unlock_door(request):
        print('Unlocking door...')
        io.unlock_door()
        utils.send_response(server, "door unlocked!", http_code=200)

    def ring_bell(request):
        print('Ringing bell...')
        io.ring_bell()
        utils.send_response(server, "bell rang!", http_code=200)

    def check_auth_key(request, address):
        if utils.get_request_auth_key(request) != config.HTTP_AUTH_KEY:
            utils.send_response(server, "Unauthorized", http_code=401)
            return False
        return True

    server.add_route("/health", lambda req: utils.send_response(server, "OK", http_code=200))
    server.add_route("/unlock_door", unlock_door)
    server.add_route("/ring_bell", ring_bell)

    if getattr(config, "HTTP_AUTH_KEY"):
        server.on_request(check_auth_key)

    server.start()
