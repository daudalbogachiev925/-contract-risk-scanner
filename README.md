# -contract-risk-scanner
Описание: сервис анализа юридических документов: PDF/DOCX → извлечение рисков, NER, отчёт для юристов. REST API + React-фронт + MinIO-хранилище.  Стек: Python 3.11, FastAPI, spaCy, pypdf, PostgreSQL, MinIO, React (Vite), Docker.


# contract-risk-scanner

Анализатор юридических рисков в договорах.

## Возможности
- Загрузка PDF, DOCX, TXT
- Автоизвлечение 10+ категорий рисков
- NER: организации, суммы, даты, лица
- Скоринг риска и уровень
- Рекомендации для юристов
- Хранение в MinIO

## Быстрый старт

cp .env.example .env
docker-compose up --build

API: http://localhost:8000/docs
UI: http://localhost:5173
MinIO: http://localhost:9001

## Пример

curl -F "file=@contract.pdf" http://localhost:8000/api/contracts/upload

## Тесты

cd backend && pytest -v

## Лицензия
MIT
