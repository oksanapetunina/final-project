#Автоматизация тестирования Kinopoisk (UI + API)
##Финальный проект курса «Инженер по тестированию» (Skypro): фреймворк автотестов для расширенного поиска фильмов на Kinopoisk.

#Что внутри:

UI‑тесты на Selenium WebDriver (Chrome): проверка поиска фильмов, валидации форм и граничных сценариев.
API‑тесты на requests: проверка статус‑кодов, структуры и значений ответов Kinopoisk API.
Allure‑отчёты с шагами и приложениями для наглядной отчётности.
Работа с БД через SQLAlchemy для валидации данных (если использовала — оставь, иначе убери).

#Стек: Python, pytest, selenium, requests, sqlalchemy, allure, webdriver‑manager.

#Структура проекта:

./tests — автотесты;
./pages — классы с методами для API и UI (Page Object);
conftest.py — фикстура для браузера Chrome;
pytest.ini — конфигурация и маркеры;
conf.ini — параметры окружения.
Как запустить:

#Как запустить:

git clone https://github.com/oksanapetunina/final-project.git
pip install -r requirements.txt   # или отдельные пакеты: pytest, selenium, webdriver-manager, allure-pytest
pytest
allure generate allure-files -o allure-report
allure open allure-report


# Автоматизация тестирования Kinopoisk (UI + API)

Финальный проект курса «Инженер по тестированию» (Skypro): фреймворк автотестов для расширенного поиска фильмов на Kinopoisk.

**Дополнительно:** полный набор артефактов ручного тестирования и примеры отчётов — [посмотреть в портфолио](https://petuninaoa-qa109-1-skypro.yonote.ru/share/d5f9fae5-1092-4f2f-a6cb-6bf505d1bdb2).

