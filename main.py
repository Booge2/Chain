import socket


def main():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Сервер запущено...")

    while True:
        client, addr = server_socket.accept()
        print(f"З’єднано з {addr}")

        while True:
            message = client.recv(1024).decode()
            print(f"Клієнт: {message}")

            if message.strip().lower() == "exit":
                break


            reply = input("Відповідь: ")
            client.send(reply.encode())



        client.close()


if __name__ == "__main__":
    main()
