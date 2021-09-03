import socket

while True:
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = 4999
    BUFFER_SIZE = 4096

    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind((SERVER_HOST, SERVER_PORT))

    s.listen(5)
    print(f"[SERVER] Listening on {SERVER_HOST}:{SERVER_PORT}")

    client_socket, address = s.accept()

    print(f"[+] INCOMING CONNECTION FROM: {address}")
    print("Saving IP....")

    file="folder/folder/logs.txt"

    with open(file, 'a') as f:
        f.write(str(address) + str("\n"))

    client_socket.send("Logged IP".encode())
    print("Saved IP")
    client_socket.close()
    s.close()
