# Liskov Substitution Principle
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
