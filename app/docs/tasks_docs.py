get_tasks = {
    "summary": "Получить список задач",
    "description": "Возвращает все задачи, созданные в системе.",
    "status_code": 200
}

get_task = {
    "summary": "Получить задачу по ID",
    "description": "Возвращает задачу по её уникальному идентификатору.",
    "status_code": 200
}

create_task = {
    "summary": "Создать задачу",
    "description": "Создаёт новую задачу, привязанную к пользователю.",
    "status_code": 201
}

update_task = {
    "summary": "Обновить задачу",
    "description": "Обновляет поля задачи по её ID.",
    "status_code": 200
}

delete_task = {
    "summary": "Удалить задачу",
    "description": "Удаляет задачу по её ID.",
    "status_code": 204
}