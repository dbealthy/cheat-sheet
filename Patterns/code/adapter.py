def get_client_card(client_id):
    return 1, 2, 3


PRODUCT_PAYMENT_CREDS = {"visa": 123123123, "mastercard": 898978734}


class PaymentGateway:

    def __init__(self, client_id): ...

    def process_payment(self, amount: float): ...


class VisaPaymentService:
    def __init__(self, card_number, expire_date, cvv):
        self.card_number = card_number
        self.expire_date = expire_date
        self.cvv = cvv

    def pay(self, amount: float, account_num: int):
        print(f"Transfer from account {self.card_number} to {account_num}: {amount}")


class ViasaPaymentGateway(PaymentGateway):
    def __init__(self, client_id):
        self.client_id = client_id
        card_number, expire_date, cvv = get_client_card(client_id)
        self.visa_service = VisaPaymentService(card_number, expire_date, cvv)

    def process_payment(self, amount: float):
        self.visa_service.pay(amount, PRODUCT_PAYMENT_CREDS["visa"])


class Client:
    def __init__(self):
        self.id = 0
        self.payment_gateway = ViasaPaymentGateway(self.id)

    def make_payment(self, amount: float):
        self.payment_gateway.process_payment(amount)


if __name__ == "__main__":
    client = Client()
    client.make_payment(1000)
