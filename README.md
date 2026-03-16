# Student Session Analytics

Простой Python CLI-проекта для анализа данных по студентам (сохранение отчета медианного расхода кофе).

## Что сделано

- Написан модуль `coffee_report.reader` для чтения CSV файлов с полями:
  - `student`, `date`, `coffee_spent`, `sleep_hours`, `study_hours`, `mood`, `exam`
- Определена модель `Record` в `coffee_report.models`.
- Реализован базовый интерфейс отчета `BaseReport` в `coffee_report.reports.base_report`.
- Реализован отчет `MedianCoffeeReport` в `coffee_report.reports.median_coffee`.
  - Он группирует записи по студенту и считает медиану расходов на кофе для каждого студента.
  - Результат сортируется по медиане кофе от большого к меньшему.
- В файле `coffee_report.reports.report_registry` зарегистрирован отчет `median-coffee`.
- В `coffee_report.main` реализован CLI:
  - аргумент `--files` — список CSV файлов
  - аргумент `--report` — ключ отчета (например, `median-coffee`)
  - вывод результата через `tabulate`.

## Как работает

1. `main.py` парсит аргументы.
2. `read_files` читает CSV и конвертирует каждую строку в объект `Record`.
3. Отчет создается через реестр `REPORTS[--report]()`.
4. `generate(records)` возвращает список кортежов `(student, median_coffee_spent)`.
5. Результат печатается в табличном виде.

## Структура проекта

- `coffee_report/`
  - `main.py` — CLI точка входа
  - `reader.py` — чтение CSV
  - `models.py` — модель `Record`
  - `reports/`
    - `base_report.py` — абстрактный класс отчета
    - `median_coffee.py` — реализация медианного отчета
    - `report_registry.py` — маппинг ключей-отчетов
- `data/` — пример CSV данных
- `tests/` — тесты

## Быстрый запуск

1. Убедитесь, что установлен Python 3.10+.
2. Установите зависимость `tabulate`:

```bash
python -m pip install tabulate
```

3. Запустите проект на файлах, например:

```bash
python -m coffee_report.main --files data/math.csv data/physics.csv data/programming.csv --report median-coffee
```

4. Если хотите запускать код как пакет:

```bash
python -m coffee_report.main --files data/math.csv --report median-coffee
```

## Тестирование

Запустите тесты:

```bash
python -m pytest
```

## Примеры CSV

Формат данных в CSV должен содержать заголовки (в любом порядке при условии, что все ключи присутствуют):

- `student`
- `date`
- `coffee_spent`
- `sleep_hours`
- `study_hours`
- `mood`
- `exam`

## Что можно добавить дальше

- Еще отчеты (среднее, максимумы, корреляции).
- Проверку и обработку ошибок в CSV (пропущенные поля, неверные типы).
- Возможность вывода в JSON/CSV.
