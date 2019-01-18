#!/usr/bin/env python3
import socket
from multiprocessing import Process
HOST = "localhost"
PORT = 8081
BUFFER_SIZE = 1024

payload = """GET / HTTP/1.0
Host: {HOST}

""".format(HOST="www.google.com")

def conn_socket(addr_tup):
    (family, socktype, proto, canonname, sockaddr) = addr_tup
    try:
        s = socket.socket(family, socktype, proto)
        s.connect(("localhost", 8081))
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)
        full_data = b""
        while True:
            data = s.recv(BUFFER_SIZE)
            if not data:
                break
            full_data += data
            print (full_data)
    except:
        pass
    finally:
        s.close()


def main():
    addr_info = socket.getaddrinfo(HOST, PORT, proto=socket.SOL_TCP)
    while True:
            p = Process(target = conn_socket, args = (addr_info))
            p.daemon = True
            p.start()
if __name__ == "__main__":
    main()
