# На стороне БД
База обеспечивает консистентную генерацию ID


# На стороне клиента


# На стороне Backend приложения


## CA
https://stackoverflow.com/questions/14082532/identity-conflict-in-ddd-with-repository
В чистой архитектуре чаще всего используется генерация id через uuid, что позволяет генерировать id во время создания сущности

Так же в некоторых случаях генерация id происходит на уровне БД, и тогда репозиторий сеттит  id для entity
Пример на CA:
https://github.com/ivan-borovets/fastapi-clean-example/issues/30

Идеальное решение для генерации на стороне базы

1. Value object for ID
``` python
@dataclass(frozen=True, repr=False)
class UserId(ValueObject):
    value: int
```

2. User Service
``` python
def create_user(self, ...) -> User:
    user_id = UserId(0)
    ...
    return User(id_=user_id, ...)
```

3. Users Table Mapping
``` python
users_table = Table(
    "users",
    mapping_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    ...
)

def map_users_table() -> None:
    mapping_registry.map_imperatively(
        User,
        users_table,
        properties={
            "_id_raw": users_table.c.id,
            "id_": composite(UserId, users_table.c.id),
            ...
        },
        column_prefix="_",
    )
```
4. User Data Mapper
```
class SqlaUserDataMapper(UserCommandGateway):
    ...
    async def add(self, user: User) -> None:
        if user.id_.value == 0:
            setattr(user, "_id_raw", None)

        self._session.add(user)
```