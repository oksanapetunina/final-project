# pytest_ui_api_template

## Шаблон для автоматизации тестирования на python

## Описание
Проект содержит набор UI-тестов для расширенного поиска фильмов на Kinopoisk с использованием Selenium WebDriver для Chrome,  набор API-тестов на взаимодействие с Kinopoisk API, а также Allure для отчетности.

### Стек:
- pytest
- selenium
- requests
- _sqlalchemy_
- allure

### Структура:
./test - тесты
./pages - классы с методами для API и UI
conf.ini - параметры окружения
conftest - фикстура для браузера Chrome
pytest.ini - настройки конфигурации и маркеры

### Библиотеки (!)
- pip install pytest
- pip install selenium
- pip install webdriver-manager 
- pip install allure-pytest

### Шаги
1. Склонировать проект 'git clone https://github.com/oksanapetunina/final-project.git
2. Установить зависимости
3. Запустить тесты 'pytest'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Ссылка на финальный проект по ручному тестированию](https://petuninaoa-qa109-1-skypro.yonote.ru/doc/finalnyj-proekt-po-ruchnomu-testirovaniyu-y7CKofNtSI)
