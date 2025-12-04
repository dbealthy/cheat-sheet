# Open Closed Principle
Код (класс) должен быть открыть для расширения и закрыт для измернения.

Пример нарушения:
``` python
class PaymentProcessor:
	def _process_visa_mastercard(self, payment):
		requests.post("https://cards/pay", payment.amount, payment.card)

	def _process_paypal(self, payment):
		requests.post("https://paypal/pay", payment.amount, payment.card)
	
	def process_payment(self, payment):
		if payment.service == "visa/mastercatd":
			self._process_visa_mastercard(payment)
		elif payment.service == "paypal":
			self._process_paypal(payment)
						
```

Каждый раз, чтобы добавить новый способ оплаты нужно изменять уже написанный код process_payment

Следствия такого решения:
- Ведет к появления новых багов при расширении
- Каждый раз нужно менять уже написанный код `process_payment`, а следовательно заново его тестировать
- Когда меняется написанный код, тесты могут ломатьсья, придется переписовать тесты
- Такой класс сложно переиспользовать поскольку он имеет в себе много ненужно логики
- Создает high coupling (большую связанность), делает систему более хрупкой


Хорошее решение:
``` python
class PaymentService(ABC):
	@abstractmethod
	def process(self, payment):
		...

class VisaMasterCardPaymentService(PaymentService):
	def process(self, payment):
		requests.post("https://cards/pay", payment.amount, payment.card)

class PypalPaymentService(PaymentService):
	def process(self, payment):
		requests.post("https://paypal/pay", payment.amount, payment.card)


class PaymentProcessor:
	def __init__(self, payment_service: PaymentService):
		self._service = payment_service
		
	def process(self, payment):
		self._service.process(payment)

processor = PaymentProcessor(
	VisaMasterCardPaymentProcessor(),
	Payment(amount=1000, card="123")
)

```