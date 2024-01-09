import telnetlib
import time
import threading

# Define the host and the port
host = '192.168.1.61' # IP address of the OMRON ARCL server
port = 7171 # Port of the OMRON ARCL server
password = 'omron'

def read_from_server(tn):
    while True:
        response = tn.read_very_eager()
        if response:
            print(response.decode(), end='')
        time.sleep(0.1)  # Sleep for a short time to reduce CPU usage

tn = None

try:
    # Connect to the server
    tn = telnetlib.Telnet(host, port, timeout=5)
except Exception as e:
    print(f"Failed to connect: {e}")
    exit()

try:
    # Wait for the password prompt and send the password
    tn.read_until(b"Password: ")
    tn.write(password.encode() + b"\n")
except Exception as e:
    print(f"Failed to send password: {e}")
    exit()

try:
    # Start a new thread that reads and prints data from the server
    threading.Thread(target=read_from_server, args=(tn,)).start()

    while True:
        # Get command from user
        command = input("Enter command: ")

        # Send the command
        tn.write((command + '\r\n').encode())

        # If the command is 'exit', break the loop
        if command.lower() == 'exit':
            break
except Exception as e:
    print(f"Failed to send command or receive response: {e}")

finally:
    # Close the connection
    if tn is not None:
        tn.close()