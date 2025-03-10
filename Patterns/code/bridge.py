"""
Отправка сообщений через разные типы соц сетей
используя паттерн адаптер

"""


class Sender:
    def send(self, client_id, message): ...


class TelegramSender(Sender):
    def __init__(self, app_id: str, token: str):
        self.app_id = app_id
        self.token = token

    def send(self, client_id, message):
        print(f"Send telegram message: {message} to {client_id}")


class ClientNotifier:
    def __init__(self, sender: Sender):
        self.sender = sender

    def notify_client(self, client_id):
        self.sender.send(client_id, "NOTFIED")


if __name__ == "__main__":
    sender = TelegramSender("abc", "123")
    notifer = ClientNotifier(sender)
    notifer.notify_client(123)
