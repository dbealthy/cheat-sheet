Для реализации хэш таблицы необходим продуманный механизм разрешения коллизий для операций чтения/записи.

В python используется стратегия **open addressing**, которая заключается в probing (переборе соседних пустых ячеек)

Хэш таблица представляет собой единый блок памяти (как массив), что позволяет выполнять операции чтения по индексу за  O(1).

Каждый слот хэш таблицы может содержать всего один элемент.
Каждый элемент таблицы это hash, key, value - реализованные как C структура.
 
- По умолчанию в cPython размер хэш таблицы составляет 8 слотов.
- При добавлении элемента в словарь python вычисляет hash значения и выбирает слот согласно полученому значению
- Если слот пуст, python записывает значение туда
- Если слот уже занят, следовательно ключ имеет такой же hash, cpython сравнивает ключи (через оператор `==`) а так же хэши
- Если значения ключений и хэшей совпадают, то python считает их одними и теме же записями в хеш таблице.
- Для записи если ключи не совпадают, cpython начинает исследовать все соседние элементы, пока не найдет свободую ячейку.
- Для чтения исользуется такой же подход, при совпадении хэшей но несовпадении ключей, cpython продолжает поиск ячейки с нужным элементом, согласно алгоритму пробинга

Алгоритмы пробинга:
- Линейный перебор i + 1
- Квадратичный перебор
- Двойной хэш (шаг расчитывается через вычисление хеша второй хэх функцией)
- Псевдо рандомный сдвиг (дефолтный подход в  python)

Когда CPython  