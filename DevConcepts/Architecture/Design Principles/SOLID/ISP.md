# Interface Segregation Principle
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
