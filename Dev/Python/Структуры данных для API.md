
- dataclass - внутренняя логика, entity, value_object, dto
  
- TypedDict - PATCH request с пропущенными аргументами. Позволяет избежать проблемы с dataclass, когда не понятно поле специально сетит значение в None или оно просто отсутствует. Так же отлично работает для моделей только для чтения (QueryModel), легче и быстрее чем dataclass. Так же позволяет переиспользовать повторяющийся аргументы в функциях
  
``` python
from typing import TypedDict, Unpack


class Options(TypedDict):
    option1: int
    option2: str


def my_function(**options: Unpack[Options]) -> None:
```
  
- pydantic - валидация типов. FaspiApi автоматически приводит dataclass и TypedDict к pydantic, валидирует данные и предоставляет документацию OpenAPI