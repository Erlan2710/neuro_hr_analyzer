# Neuro HR Analyzer

Модульное приложение на Python для извлечения и обработки текста собеседований с использованием GPT и LangChain.

## Возможности

- Загрузка текста интервью из Google Docs (формат `.txt`)
- Обработка и очистка текста
- Интеграция с OpenAI GPT через LangChain
- Возможность разбиения текста на сегменты (для embedding)
- Поддержка `.env` для безопасного хранения ключей

## Технологии

- Python 3.10+
- OpenAI API (gpt-4o-mini)
- LangChain
- tiktoken
- python-dotenv
- requests

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/YOUR_USERNAME/neuro_hr_analyzer.git
cd neuro_hr_analyzer
```

2. Установите зависимости:

```bash
pip install -r requirements.txt
```

3. Создайте файл `.env` в корне проекта и добавьте ваш OpenAI API ключ:

```env
OPENAI_API_KEY=sk-ваш_ключ
```

4. Запустите проект:

```bash
python main.py
```

## Планы на развитие

- Добавление аудиоанализа (Whisper + Silero VAD)
- Диаризация спикеров
- Генерация структурированных резюме и писем
- Внедрение агентной архитектуры