import socket

def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("localhost", 8888))
        s.send(command.encode())
        response = s.recv(1024).decode()
        print("Response:", response.strip())

def main():
    while True:
        user_input = input("Enter command (e.g., SET key value, GET key, DELETE key, MSET key1 value1 key2 value2, MGET key1 key2, PUT {key: value}, SHOW): ")
        send_command(user_input)

if __name__ == "__main__":
    main()
