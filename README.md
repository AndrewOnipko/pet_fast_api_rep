# Task API

Асинхронный REST API пет проект на FastAPI для управления задачами и пользователями.  

---

## Технологии

- **Python** 3.11+
- **FastAPI**
- **SQLAlchemy 2.0 (Async)**
- **SQLite** (встроенная БД, для простоты)
- **Pydantic v2**
- **Uvicorn**
- Логирование через `logging` + кастомный декоратор `simple_logger`
- Структурированный код:
  - `routers/` — маршруты
  - `services/` — бизнес-логика
  - `repositories/` — работа с БД
  - `schemas/` — валидация и сериализация
  - `models/` — ORM-модели
  - `docs/` — документация

---

## Запуск

1. Клонируйте репозиторий  
2. Установите зависимости:
   pip install -r requirements.txt

3. Запустите приложение:
```bash
uvicorn app.main:app --reload
```
   * Через VSCode можно запустить через Run/Debug конфигурацию (launch.json)

4. Откройте документацию:
   Swagger: http://localhost:8000/docs
   Redoc: http://localhost:8000/redoc

## Функциональность

# Пользователи /users

* GET /users — список всех пользователей

* GET /users/{id} — один пользователь

* POST /users — создать

* PUT /users/{id} — обновить

* DELETE /users/{id} — удалить

# Задачи /tasks

* GET /tasks — список задач

* GET /tasks/{id} — одна задача

* POST /tasks — создать

* PUT /tasks/{id} — обновить

* DELETE /tasks/{id} — удалить

## Примечания

- Все запросы и операции логируются в logs.log

- Структура и подход демонстрируют продвинутые практики backend-разработки
