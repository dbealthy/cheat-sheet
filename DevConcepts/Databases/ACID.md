Набор требований к транзакционной системе обеспечивающий наиболее надежную и предсказуемую работу.

```
A - atomicity
C - consistency
I - isolation
D - durability
```


**A** - Гарантирует, что никакая транзакция не будет зафиксирована в системе частично (Принцип все или ничего) Если одна из операций вызовет ошибку, все транзакия будет отменена (rollback)

**C** - Транзакция, достигая состояние нормального завершения (EOT) фиксирует свои резуьтаты, сохраняя согласованность в базе, не давая перейти базе в несогласованное состояние. 
ACID СУБД поддерживают стандартные механизмы поддержания согласованности через констрейнты, внешние ключи..., но  СУБД не может гарантировать согласованность данных с бизнес требованиями, следовательно за согласованность отвечает уровень приложения и его программист.

**I** - Во время выполнения транзакции, параллельные транзакции не должны оказывать влияния на ее результат. Для достижения изоляции базу поддерживают различные уровни изоляции
	- Read uncommitted
	- Read committed (по умолчанию в большенстве СУБД)
	- Repeatable read (snapshot, данные не могут быть изенены во временя транзакции)
	- Serializable (блокирует строки, так что транзакциии операции чтения записи выполняются последовательно. Блокируются все операции, даже на добавление записей)

![[Pasted image 20240628095019.png]]


**D** - Независимо от проблем на нижних уровнях (обесточивание системы, сбои в оборудовании) изменения, сделанные успешно завершенной транзакцией, должны оставаться сохраненными мосле возвращения системы в работу. 

(Гарантия сохранности изменений после успешного завершения транзакции)


## Выставление уровня изоляции

- PyMysql:
	`cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;")`
	
- SqlAlchemy
	`engine = create_engine( "mysql+pymysql://user:password@localhost/test_db", isolation_level="READ COMMITTED" # Уровень изоляции )`
	
- Django ORM
	`DATABASES = { 'default': { 'ENGINE': 'django.db.backends.mysql', 'NAME': 'test_db', 'USER': 'user', 'PASSWORD': 'password', 'HOST': 'localhost', 'PORT': '3306', 'OPTIONS': { 'isolation_level': 'read committed', # Уровень изоляции }, } }`
	
	Или для курсора
	`cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;")`