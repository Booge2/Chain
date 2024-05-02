import socket


# def main():
#     host = "127.0.0.1"
#     port = 12345
#
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client.connect((host, port))
#
#     while True:
#         message = input("Введіть повідомлення: ")
#         client.send(message.encode())
#
#         if message.strip().lower() == "exit":
#             break
#
#         reply = client.recv(1024).decode()
#         print(f"Сервер: {reply}")
#
#     client.close()
#
#
# if __name__ == "__main__":
#     main()
# Завдання 2


# def main():
#     host = "127.0.0.1"
#     port = 12345
#
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect((host, port))
#
#     country = input("Введіть країну: ")
#     city = input("Введіть місто: ")
#
#     client_socket.send(f"{city},{country}".encode())
#
#     response = client_socket.recv(1024).decode()
#     print(response)
#
#     client_socket.close()
#
#
# if __name__ == "__main__":
#     main()
# Завдання 3


def main():
    host = "127.0.0.1"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    text = input("Введіть текст для перекладу: ")
    target_language = input("Введіть код цільової мови: ")

    client_socket.send(f"{text},{target_language}".encode())

    translated_text = client_socket.recv(1024).decode()
    print("Переклад:", translated_text)

    client_socket.close()


if __name__ == "__main__":
    main()
