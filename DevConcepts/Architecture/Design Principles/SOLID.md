# 1. Single Responsibility Principle
Код (класс) должен иметь одну и только одну ответственность, а следовательно через него должно проходить только одна ось изменений.

Пример нарушения:
``` python
class ReportGenerator:
	def generate_analytics_report(self):
		response = requests.get("https://an.com")
		data = response.json()
		report = Report(data["statistics"], data["event"])
		table = excel.make_table(columns=["stats", "event"], data=report.dict())
		table.write("result.xlsx")
		
```

Класс делает сразу три вещи:
- Получает данные из интернета
- Формирует оъект отчета
- Записывает excel таблицу в файл

Следствия такого решения:
- Если нужно изменить формат таблицы или изменить тип генерируемого файла, иди делать запрос не по http, а в базу, придется изменять всю функцию
- Код очень сложно тестировать, т.к. придется тестировать функцию целиком и переделовать тесты при малейшем изменении
- Невозможно переиспользовать логику для получение данных отчета или логику формирование таблиц
- Сложно масштабировать т.к. функционал классно нельзя переиспользовать. И попытка расширения приведет к повторению кода
- Сложно читать и понимать, тяжело поддерживать такой код работая в команде.

Хорошее решение:
``` python
class ReportGateway(ABC):
	@abstractmethod
	def get_report(self) -> Report:
		...
	
class AnaliticsReportGateway(ReportGateway):
	def __init__(self, url, token):
		self._url = url
		self._token = token
		
	def get_report(self) -> Report:
		response = requests.get(self._url, headers={"token": token})
		data = response.json()
		return Report(data["statistics"], data["event"])

class ReportWriter(ABC):
	@abstractmethod
	def wirte(self, report: Report):
		...
class ExcelReportWriter(ReportWriter):
	def __init__(self, output_path: str):
		self._output_path = output_path

	def write(self, report: Report):
		table = excel.create_table(columns=["stats", "event"], report.dict())
		table.write(self._output_path)

class ReportGenerator:
	def __init__(self, report_gateway, report_writer):
		self._gateway = report_gateway
		self._writer = report_writer
	
	def generate_analytics_report(self):
		report = self._gateway.get_report()
		self._writer.write(report)

ReportGenerator(
	AnaliticsReportGateway("https://analytics.com", "abc"),
	ExcelReportWriter("result")
)

```


# 2. Open Closed Principle
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


# 3. Liskov Substitution Principle
Любой дочерний класс должен быть заменяем любым другим дочерним классом того же родителя без каких либо сайд эффектов.

Т.е. дочерние классы должны полностью следовать контракту(протоколу) базового класса

Пример нарушения:
``` python
class DeviceError(Exception):
	...

class BrokenBulbError:
	...

class Controller:
	def get_info(self, device) -> DeviceInfo:
		result = device.get_info()
		if isinstance(result, dict):
			return DeviceInfo(**result)
		elif isinstance(result, DeviceInfo):
			return result
		raise ValueError
	
	def turn_on(self, device):
		try:
			device.turn_on()
		except DeviceError as err:
			self.light_red_led()
			raise err
		
	def turn_off(self, device):
		device.turn_off()

class Device(ABC):
	@abstractmethod
	def get_info(self) -> DeviceInfo:
		...

	@abstractmethod
	def turn_on(self):
		...

	@abstractmethod
	def turn_off(self):
		...

class Bulb(Device):
	def __init__(self, state):
		self._state = state
		
	def get_info(self) -> dict:
		return DeviceInfo{"madein": "USSR"}

	def turn_on(self):
		if self._state == "broken":
			raise BrokenBulbError
		self._turn_on()
		
	def tunr_off(self):
		self._turn_off()

ctl = Controller()
ctl.turn_on(Bulb(state="broken"))
ctl.get_info(Bulb(state="ok"))

```

В коде есть 3 нарушения:
- Подкласс Bulb в методе get_info возвращает словарь, вместо DeviceInfo
- Подкласс Bulb возбуждает исключение, которое не предусмотрено базовым классом, а так же не ожидается клиентами BrokenBulbException
- Клиент вынужен по разному обрабатывать подтипы device, в зависимости от ответа.

Следствия такого решения:
- Ломается полеморфизм. Баги, которые сложно отловить. Такие классы могут полностью положить клиентский код, который их использует.
- Дополнительная логика для обработки разных подтипов внутри клиентского кода
- Нарушается OCP, т.к приходтся менять код при добавлении подклассов
- Сложно тестировать, т.к. нет гарантии, что если один подкласс прошел тесты, то и другой пройдет. Дублирование тестов
- Код становится хрупким и его становится невозможно рефакторить, т.к. не понятно к каким последствиям это может привести. Например при добавлении подкласса SmartBulb, наследника Bulb

Хорошее решение:
``` python
class DeviceError(Exception):
	...
class BrokenBulbError(DeviceError):
	...

class Controller:
	def get_info(self, device) -> DeviceInfo:
		return device.get_info()
	
	def turn_on(self, device):
		try:
			device.turn_on()
		except DeviceError as err:
			self.light_red_led()
			raise err
		
	def turn_off(self, device):
		device.turn_off()

class Device(ABC):
	@abstractmethod
	def get_info(self) -> DeviceInfo:
		...

	@abstractmethod
	def turn_on(self):
		...

	@abstractmethod
	def turn_off(self):
		...

class Bulb(Device):
	def __init__(self, state):
		self._state = state
		
	def get_info(self) -> dict:
		return DeviceInfo(made_in="USSR")

	def turn_on(self):
		if self._state == "broken":
			raise BrokenBulbException 
		self._turn_on()
		
	def tunr_off(self):
		self._turn_off()

ctl = Controller()
ctl.turn_on(Bulb(state="broken"))
ctl.get_info(Bulb(state="ok"))
```

# 4. Interface Segregation Principle
Много маленьких интерфейсов, по интерфейсу для каждого клиента лучше чем один большой для всех. При изменении метода интерфейса, не должны меняться программные сущности, которые этот метод не используют

Пример нарушения:
``` python
class Vehicle(ABC):
	@abstractmethod
	def start(self):
		...
		
	@abstractmethod
	def stop(self):
		...

	@abstractmethod
	def turn_on_radio(self):
		...

class Car(Vehicle):
	def start(self):
		self.engine.start()

	def stop(self):
		self.engine.stop()

	def turn_on_radio(self):
		self.radio.turn_on()

class Bicycle(Vehicle):
	def start(self):
		self.wheels.rotate()

	def stop(self):
		self.breaks.stop()

	def turn_on_radio(self):
		raise NotImplemented
```

В коде есть нарушение:
- Велосипед обязан реализововать метод turn_on_radio, который ему не нужен
- Если понадобится добавить еще один метод, который не подходит для велосипеда в интерфейсе, то велосипеду снова придется возвращать ошибку NotImplemented

Следствия такого решения:
- Ложные зависимости, от кода который не нужен
- Усложняется тестирование из за того, что нужно мокать еще и неиспользуемые методы
- Больше кода и сложнее поддержка
- Нарушение принципа OCP. Т.к при изменении нитерфейса приходится менять все классы, которые его наследуют, но не используют логику

Правильное решение:
``` python
class Vehicle(ABC):
	@abstractmethod
	def start(self):
		...
		
	@abstractmethod
	def stop(self):
		...

class EmbededRaiod(ABC):
	@abstractmethod
	def turn_on_radio(self):
		...

class Car(Vehicle, EmbededRaiod):
	def start(self):
		self.engine.start()

	def stop(self):
		self.engine.stop()

	def turn_on_radio(self):
		self.radio.turn_on()

class Bicycle(Vehicle):
	def start(self):
		self.wheels.rotate()

	def stop(self):
		self.breaks.stop()

	def turn_on_radio(self):
		raise NotImplemented
```

# 5. Dependency Inversion Principle
Классы не должна зависить от конкретных деталей, а должны зависить от абстракций. 

Т.е в классах верхнего уровня, не должно быть импортов кода нижнего уровня (конкретной БД, метода млатежа, или внешнего сервиса) 

Принцип снижает осведомленность о данных и поведении объекта (и coupling с ним) до минимума, описанного в интерфейсе.

Формулировка:
- A. High level modules should not depend upon low level modules. Both should depend upon abstractions.
- B. Abstractions should not depend upon details. Details should depend upon abstractions.

---
В традиционной 3-х слойной архитектуре компоненты более высокого уровня импортируют код из более низкого уровня
[![](https://upload.wikimedia.org/wikipedia/commons/4/42/Traditional_Layers_Pattern.png)](https://en.wikipedia.org/wiki/File:Traditional_Layers_Pattern.png)

В таком случае компоненты более высокого уровня напрямую зависят от деталей (utility), что приводит к большей связности и усложнаяет вохможности переиспользования и тестирования

---
Применяя DIP
Компоненты высокого уровня не зависят от компонентов низкого уровня, и компоненты низкого и высокго уровня зависят от абстракции

[![](https://upload.wikimedia.org/wikipedia/commons/8/8d/DIPLayersPattern.png)](https://en.wikipedia.org/wiki/File:DIPLayersPattern.png)

Интерфейсы принадлежат к модулям более верхнего уровня и хранятся вместе с ними, а детали реализации должны их импортировать и реализововать

Когда нужно сделать инверсию зависимостей для закрытого кода (зависимости которого переделать нельзя) или уже написанного кода, то часто используется паттерн **Adapter**

Пример нарушения
``` python
class Shop:
	def __init__(self, creds):
		self._database = MysQLDB(creds)
	
	def get_product(self, id):
		return self._database.get_product, id=id)
		
shop = Shop(...)
shop.get_product(1)
```
В коде есть нарушение:
- Класс верхнего уровня зависит от деталей реализации конкретной базы данных.
- Класс нижнего уровня знает о деталях верхнего уровня

Следствия такого решения:
- Сложно изменить базу данных напрмер на Posgresql или вообще на REST API.
- Сложно тестировать, т.к. придется делать вызовы в базу данных
- Жесткая связанность между Shop и базой данных, т.к. оба знают ненужные им детали.

Правильное решение
``` python

class ShopRepository(ABC):
	@abstractmethod
	def get_product(self, id):
		...

class Shop:
	def __init__(self, shop_repository: ShopRepository):
		self._repo = shop_repository
		
	def get_prodcut(self, id):
		return self._repo.get_product(id)
		
# Details
class MySQLShopRepository(ShopRepository):
	def __init__(self, creds):
		self._db = MysQLDB(creds)
		
	def get_product(self, id):
		return self._database.get_product, id=id)

shop = Shop(MySQLShopRepository(...))
shop.get_prodcut(1)
```
