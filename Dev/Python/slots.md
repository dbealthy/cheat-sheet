Для оптимизации потребляемой памяти приложением, можно использовать свойство `__slots__` при объявлении класс.

``` python
class Normal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        

class Slotted:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

За счет этого свойства python выделяет фиксированный объекм памяти, необходимый только для указанных стройства и не создает `__dict__` за счет чего происходит значительная экономия памяти

## Недостатки и особенности
- Нельзя динамиески добавлять поля в объект
- При наследовании и родительский и дочерний классы должны быть со свойством `__slots__`, причем дочерний класс должен определить поля, которые специфичны именно ему.
- При наследовании нужно передавать родельский аргументы при вызове `super().__init__(paren_args)`
``` python
class Parent:
    __slots__ = ('a',)
    def __init__(self, a):
        self.a = a

class Child(Parent):
    __slots__ = ('b',)
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

child = Child(1, 2)
try:
    child.c = 3  # Ошибка, потому что 'c' не объявлен ни в Parent, ни в Child
except AttributeError as e:
    print("Ошибка:", e)
```
  
- Слоты по умолчанию не поддерживаю слабые ссылки
  
``` python
class WeakSlotted:
    __slots__ = ('x', 'y', '__weakref__')
    def __init__(self, x, y):
        self.x = x
        self.y = y

import weakref

obj = WeakSlotted(100, 200)
ref = weakref.ref(obj)
print("Слабая ссылка:", ref())
```



## Интеграция с dataclass

``` python
from dataclasses import dataclass

@dataclass(slots=True)
class Point:
    x: int
    y: int

p = Point(10, 20)
print(f"Point: ({p.x}, {p.y})")
try:
    p.z = 30  # Попытка добавить новый атрибут
except AttributeError as e:
    print("Ошибка:", e)
```