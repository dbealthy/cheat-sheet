Source: https://www.reddit.com/r/dotnet/comments/16vbqa3/vertical_slice_architecture_and_shared/, https://bool.dev/blog/detail/obzor-vertical-slice-architecture

Организация структуры проекта по фичам, а не по технологиям или техническим категориям

```plaintext
ProjectName/
│
├── Features/
│   ├── UserAuthentication/
│   │   ├── Controllers/
│   │   ├── Services/
│   │   ├── Models/
│   │   ├── Repositories/
│   │   └── Data/
│   ├── FlightBooking/
│   │   ├── Controllers/
│   │   ├── Services/
│   │   ├── Models/
│   │   ├── Repositories/
│   │   └── Data/
│   └── HotelReservations/
│       ├── Controllers/
│       ├── Services/
│       ├── Models/
│       ├── Repositories/
│       └── Data/
└── Shared/
    ├── Utilities/
    └── Middleware/
```

Adaptation for Django projects

```
project/
├── apps/
│   └── crediting/            # Bounded context (domain)
│       ├── domain/
│       │   └── loan.py       # Entities, VOs, domain logic
│       ├── application/
│       │   └── commands/
│       │       └── approve_loan.py  # Use cases
│       ├── infrastructure/
│       │   └── repositories.py  # Django ORM, adapters
│       └── presentation/
│           ├── views.py      # DRF views
│           └── serializers.py
├── config/
│   └── settings/

```

## Основные идеи
- Vertical Sliced Architecture группирует код по важным для бизнеса фичам.
- **[[4. Low Coupling]] и [[5. High Cohesion]] между модулями**.
- Каждая бизнес фича выделена в отедльный срез (slice), который включает в себе контроллеры, модели, сервисы, бизнес логику, репозитории, доменные сущности, ...
- На практике можно использовать комбинацию DDD, CA, VSA. Разбить проект на домены (ddd. bounded context), внутри каждого домена разбить структуру по фичам (vsa), и внутри каждой фичи можно сделать CA
- Feature-Centric Design - альтернативное название для VSA
- Каждый срез (фича), сам решает, какую архитекутуру внутри себя использовать. Но предпочтительнее использовать Clean Architecture.
- По умолчанию предпологается, что срезы (фичи) изолированы друг от друга, чтобы уменьшить coupling, но VSA не ограничивает в возможности переиспользования кода между фичами. Для этого есть несколько подходов:
	- Event Driven Architecture (предпочтительно). Фича публикует событие, а другая фича обрабатывает его, тем самым не увеличивая coupling
	- Shared/Common directory. Общая логика между фичами, которая меняется по одним и тем же причинам для разных фичей (Auth, DataAccess)
	- Прямая зависимость между фичами не запрещена, просто это не выбор по умолчаню, тогда как в чистой архитектуре - это выбор по умолчанию. Отложить решение о прямой зависимости между модулями (переиспользовании), а не устранить его.
	  
	  > Slices doesn’t mean sharing isn’t allowed. It’s just not the default choice. Whereas a layered approach means sharing is the default choice. I want to defer the sharing decision, not eliminate it.
	  > 
	  > Jimmy Bogart (создатель концепции)
	  
- Minimize communication between slices and maximize communication within a slice.
  
- The new features only add code into codebase, you don't change the overall codebase and you don't worry about side effects.
- Подход позволяет легко в будущем перейти к микросервисам, если четко следовать архитектуре, просто вынося фичи в отдельные микросервисы

![[Pasted image 20250404094619.png]]


# Преимущества
- High cohesion: Все элементы, нужные для реализации фичи лежат в одном месте, а значит их легче понимать и легче изменять
- Low coupling: Фичи слабо зависят друг от друга, упрощая изменения и тестирование
- Modularity and scalability: Новые фичи могут быть добавлены без влияния на существующий код
- Хорошо подходит для больших проектов, где работает несколько человек


## Недостатки
- Сложность разбиением бизнес требований на фичи, что требует тщательного планирования
- Возможно дублирование кода в разных фичах, т.к. программист может забыть, что такой функционал уже есть в другой фиче или не захочет добавлять лишнюю связанность
- Сложность с менеджментом зависимостей между компонентами, а так же и common/utilities
- В маленьких проектах может добавить лишнюю сложность

## Сравнение с чистой архитектурой
Тогда как чистая архитектура предлогает делить структуру приложения по слоям 

```
ProjectName/
|
├──	domain/
├──	application/
├──	infrastructure/
```

Почему лучше использовать структуру VSA чем CA
https://www.reddit.com/r/dotnet/comments/lw13r2/choosing_between_using_cleanonion_or_vertical/


Пример хорошей архитектуры
https://github.com/evgenirusev/.NET-Domain-Driven-Design-Template (DDD + CA + VSA)