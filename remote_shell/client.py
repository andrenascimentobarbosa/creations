import socket

# Define the server's IP address and port
SERVER_HOST = '127.0.0.1' # Server IP address
SERVER_PORT = 4444 # Server Port

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Start receiving commands from the user
while True:
    # Get the command from the user
    command = input(f"remote_shell@{SERVER_HOST}: ")

    # Send the command to the server
    client_socket.send(command.encode())

    # If the command is 'exit', break the loop
    if command.lower() == 'exit':
        break

    # Receive the output from the server and print it
    output = client_socket.recv(1024).decode()
    print(output)

# Close the socket
client_socket.close()
