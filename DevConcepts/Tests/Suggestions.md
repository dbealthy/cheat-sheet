Использовать create_autospec что быстро создаваь моки из классов.
``` python
from unittest.mock import create_autospec
from app import UserService

user_service = create_autospec(UserService)
user_service.is_password_valid.return_value = True

# Или ошибка
user_service = create_autospec(UserService)
user_service.is_password_valid.side_effect = ValueError("...")

```

