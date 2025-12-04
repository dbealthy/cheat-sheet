# Single Responsibility Principle
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
