import socket

# Creiamo un dizionario per memorizzare i dati
database = {}

def handle_client(client_socket):
    while True:
        request = client_socket.recv(1024).decode()
        if not request:
            break
        parts = request.split()
        command = parts[0]
        if command == "SET":
            key = parts[1]
            value = " ".join(parts[2:])
            database[key] = value
            client_socket.send(b"OK\n")
        elif command == "GET":
            key = parts[1]
            value = database.get(key, "NULL")
            client_socket.send(value.encode() + b"\n")
        elif command == "DELETE":
            key = parts[1]
            if key in database:
                del database[key]
                client_socket.send(b"OK\n")
            else:
                client_socket.send(b"Key not found\n")
        elif command == "MGET":
            keys = parts[1:]
            values = [database.get(key, "NULL") for key in keys]
            response = " ".join(values)
            client_socket.send(response.encode() + b"\n")
        elif command == "PUT":
            database.update(eval(parts[1]))
            client_socket.send(b"OK\n")
        elif command == "SHOW":
            response = "\n".join([f"{key}: {value}" for key, value in database.items()])
            client_socket.send(response.encode() + b"\n")
        else:
            client_socket.send(b"Invalid command\n")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8888))
    server_socket.listen(5)
    print("Server listening on port 8888...")
    while True:
        client_socket, address = server_socket.accept()
        print("Accepted connection from", address)
        handle_client(client_socket)

if __name__ == "__main__":
    main()
