import socket
import threading

# Get target from user
target = input("Enter the target IP address or domain name: ")

# Resolve domain to IP (if domain given)
try:
    target_ip = socket.gethostbyname(target)
    print(f"\n[INFO] Scanning target: {target_ip}\n")
except socket.gaierror:
    print("[ERROR] Invalid hostname.")
    exit()

# Scan a single port
def scan_port(port):
    try:
        # Create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # seconds

        # Attempt to connect
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        s.close()
    except:
        pass  # Ignore errors silently

# Use threading to speed up scanning
print("[INFO] Scanning ports 1 to 1024...\n")

for port in range(1, 1025):
    t = threading.Thread(target=scan_port, args=(port,))
    t.start()