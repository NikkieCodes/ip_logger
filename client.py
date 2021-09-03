import socket

s = socket.socket()

host = "127.0.0.1"
port = 4999

print(f"Connecting to {host}:{port}")
try:
    s.connect((host, port))
    print("[+] CONNECTED")

except TimeoutError:
    print("Timed out")
    input("Press enter to continue")


s.close()
print("[-] DISCONNECTED")
input("PRESS ENTER TO CONTINUE")
