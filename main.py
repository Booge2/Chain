import socket
import threading
from googletrans import Translator


# def main():
#     host = "127.0.0.1"
#     port = 12345
#
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind((host, port))
#     server_socket.listen(1)
#
#     print("Сервер запущено...")
#
#     while True:
#         client, addr = server_socket.accept()
#         print(f"З’єднано з {addr}")
#
#         while True:
#             message = client.recv(1024).decode()
#             print(f"Клієнт: {message}")
#
#             if message.strip().lower() == "exit":
#                 break
#
#             reply = input("Відповідь: ")
#             client.send(reply.encode())
#
#         client.close()
#
#
# if __name__ == "__main__":
#     main()
# Завдання 2


# def handle_client(client_socket):
#     request = client_socket.recv(1024).decode()
#
#     response = "Погода на тиждень для міста {}:\n Monday: 20°C, Tuesday: 22°C, Wednesday: 23°C, Thursday: 21°C, Friday: 19°C, Saturday: 18°C, Sunday: 20°C".format(
#         request)
#     client_socket.send(response.encode())
#
#     client_socket.close()
#
#
# def main():
#     host = "127.0.0.1"
#     port = 12345
#
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind((host, port))
#     server_socket.listen(5)
#
#     print(f"Сервер запущено на {host}:{port}")
#
#     while True:
#         client_socket, addr = server_socket.accept()
#         print(f"З'єднання від {addr[0]}:{addr[1]}")
#
#         client_handler = threading.Thread(target=handle_client, args=(client_socket,))
#         client_handler.start()
#
#
# if __name__ == "__main__":
#     main()
# Завдання 3


def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text


def handle_client(client_socket):
    request = client_socket.recv(1024).decode()
    print("Запит на переклад:", request)

    text, target_language = request.split(",")

    translated_text = translate_text(text, target_language)

    client_socket.send(translated_text.encode())

    client_socket.close()


def main():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Сервер запущено на {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"З'єднання від {addr[0]}:{addr[1]}")

        handle_client(client_socket)


if __name__ == "__main__":
    main()
