import socket

def is_port_open(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((host, port))
    except (socket.timeout, socket.error):
        return False
    else:
        return True
    finally:
        s.close()

def scan_ports(host, ports):
    open_ports = []
    for port in ports:
        if is_port_open(host, port):
            open_ports.append(port)
    return open_ports

if __name__ == "__main__":
    target_host = "example.com"  # Replace with the target host
    target_ports = [22, 80, 443]  # Replace with the list of ports you want to scan

    open_ports = scan_ports(target_host, target_ports)
    if open_ports:
        print(f"Open ports on {target_host}: {open_ports}")
    else:
        print(f"No open ports found on {target_host}")