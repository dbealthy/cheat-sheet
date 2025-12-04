Объект предметной области имеет в себе  методы для работы с инфраструктурой (БД)

User.objects.get(pk=1)
User.objects.filter(name="Joan").update(age=10)
user.save()