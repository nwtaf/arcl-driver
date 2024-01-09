import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set a timeout in seconds
s.settimeout(5.0)

# Define the host and the port
host = '192.168.1.61' # IP address of the OMRON ARCL server
port = 7171 # Port of the OMRON ARCL server

try:
    # Connect to the server
    s.connect((host, port))
except socket.error as e:
    print(f"Failed to connect: {e}")
    s.close()
    exit()

# Send a command
command = 'your_command\r\n'
try:
    s.sendall(command.encode())
except socket.error as e:
    print(f"Failed to send command: {e}")
    s.close()
    exit()

# Receive the response
try:
    response = s.recv(1024)
    if not response:
        print("No response received. The command may not be supported.")
    else:
        print('Received', repr(response))
except socket.error as e:
    print(f"Failed to receive response: {e}")

# Close the connection
s.close()