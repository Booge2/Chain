import socket

def main():
    host = "127.0.0.1"
    port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    while True:
        message = input("Введіть повідомлення: ")
        client.send(message.encode())

        if message.strip().lower() == "exit":
            break

        reply = client.recv(1024).decode()
        print(f"Сервер: {reply}")



    client.close()

if __name__ == "__main__":
    main()
