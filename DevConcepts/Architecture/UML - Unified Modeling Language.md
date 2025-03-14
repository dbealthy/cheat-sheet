# Виды диаграм
- Класс диаграмма - показывает общую структуру иерархии между классами и их кооперацию.
	Применятесят для документарования, визуализации, прямого и **обратного** проектирования
	*Самая часто используемая 90% случеев*
	
- Диаграмма последовательностей - показывает алгоритм действия какого либо процесса
  
- Остольные почти не используются


# Класс диаграмма

![Определение класса](https://media.geeksforgeeks.org/wp-content/uploads/20240118123645/Class-Notation.webp)

Так же на следующей строке после имени класса можно указать что это энам или интерфейс `<Enum>`, `<Interface>`

```
<<Interface>>
Car
---------------
+ attr1: type
- attr2: type
---------------
+ method1(): type
- method2(val: type): type
```

Знаки + и - означают уровень доступа (приватный, публичный)
## Стрелки
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Uml_classes_ru.svg/351px-Uml_classes_ru.svg.png)](https://commons.wikimedia.org/wiki/File:Uml_classes_ru.svg?uselang=ru)

Нотация UML для отображения взаимосвязи между классами на диаграммах

- Ассоциация - класс А вызывает класс Б (метод класса Б). Другими словами А зависит от Б
  
  `_____________` - линия без стрелочки. Двунаравленная циклическая ассоциация. Класс А зависит от класса Б и наоборот. Это ошбика и такого быть не должно, но часто означает что класс А **как-то зависит** от класса Б, потом разберемся как
  
- Агрегация (has a) - у класс А есть поле споисок объектов Б. 
  Например комната и мебель. Комната может существовать и без мебели. Мебель ничего не знает о комнате.

- Композиция (consists of) - более строгий тип агрегации. Означает что класс А не может существовать хотя бы без одного объекта Б
  Например дом и комната. В дома должна быть хотя бы одна комната.
  
- Наследование (генерализация/extends) - стрелка идет в направлении того от кого происходит наследование
  
- Зависимость - класс А как то зависит от класса Б (вызывает метод, обращается к переменной или как то иначе непонятно как)

# Диаграмма последовательностей
Простой пример

![Пример диаграммы последовательностей типичного backend приложения](https://habrastorage.org/r/w1560/getpro/habr/upload_files/355/aae/3f2/355aae3f266f4762d706b7a663545f19.png)