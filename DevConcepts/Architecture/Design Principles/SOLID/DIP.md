# Dependency Inversion Principle
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
