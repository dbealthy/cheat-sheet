
# Naming

- HTTP Endpoints - use plural: `/users`, `/roles`
  
- Database Tables - use plural for regular tables: `users`, `roles`, use singular + plural for junction tables: `user_roles`, `role_permissions`
  
- Add 'Error' suffix for most of the errors. ApplicationError, UsernameAlreadyExistsError, ...  
  
- UseCase - commands (create, update, delete) - "{Action}{Resource}Interactor", read use cases - "{Action}{Resource}Query"

- UseCase dtos - входные данные - {Action}{Resource}{Request}, выходные {Action}{Resource}{Response}
- Доменные сервисы - {Resource}Service
  
- Repository use singular + Repository. UserRepository. Command repository - {Resource}Repository, Query - {ResourceQueryRepository}
  
- Common models for quering ResourceQueryModel
- Parameters for querying resource {Resource}{Action}Params


# Project Structure

- One UseCase - one module
- One Service - One module
- Controllers grouped by resource in modules
