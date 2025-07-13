get_users = {
    "summary": "Получить список пользователей",
    "description": "Возвращает всех пользователей в системе.",
    "status_code": 200
}

get_user = {
    "summary": "Получить пользователя по ID",
    "description": "Возвращает одного пользователя по уникальному идентификатору.",
    "status_code": 200
}

create_user = {
    "summary": "Создать пользователя",
    "description": "Создаёт нового пользователя с переданными данными.",
    "status_code": 201
}

update_user = {
    "summary": "Обновить пользователя",
    "description": "Обновляет поля пользователя по ID.",
    "status_code": 200
}

delete_user = {
    "summary": "Удалить пользователя",
    "description": "Удаляет пользователя по ID.",
    "status_code": 204
}