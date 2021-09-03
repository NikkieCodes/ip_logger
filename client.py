import socket

s = socket.socket()

host = "shitboxnikkie.us.to"
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