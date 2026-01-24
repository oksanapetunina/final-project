import pytest
import allure
import requests
from pages.api_page import Kinopoisk_Api
import configparser


@pytest.fixture(scope="module")
def api():
    config = configparser.ConfigParser()
    config.read('conf.ini')
    base_url = config['DEFAULT']['base_url']
    token = config['DEFAULT']['token']
    return Kinopoisk_Api(base_url, token)


@allure.title("Поиск фильма по id")
@allure.description("Поиск фильма по id=298")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.positive_test_api
@pytest.mark.test_api
def test_search_movie_by_id(api):
    film_id = 302
    with allure.step("Отправить get-запрос с id = 298"):
        url = f"{api.base_url}/api/v2.2/films/{film_id}"
        headers = api.get_headers()
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        data = resp.json()

    with allure.step("проверить: в ответе код 200 и в теле kinopoiskId: 298"):
        assert resp.status_code == 200
        assert data["kinopoiskId"] == film_id


@allure.title("Поиск данных сезоне для сериала")
@allure.description("Поиск о сезоне по id=77046")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.positive_test_api
@pytest.mark.test_api
def test_search_movie_by_id(api):
    film_id = 77046
    with allure.step("Отправить get-запрос с id = 77046"):
        url = f"{api.base_url}/api/v2.2/films/{film_id}/seasons"
        headers = api.get_headers()
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        data = resp.json()

    with allure.step("проверить: " \
        "в ответе код 200 и в теле kinopoiskId: 77046"):
        assert resp.status_code == 200
        assert data["total"] == 11


@allure.title("Поиск фильма по несуществующему id")
@allure.description("Поиск фильма по id=9999999")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.negative_test_api
@pytest.mark.test_api
def test_search_movie_by_nonexistent_id(api):
    film_id = 9999999
    with allure.step("Отправить get-запрос с несуществующим id=9999999"):
        url = f"{api.base_url}/api/v2.2/films/{film_id}"
        headers = api.get_headers()
        resp = requests.get(url, headers=headers)
    with allure.step("проверка: в ответе  код 404"):
        assert resp.status_code == 404


@allure.title("Поиск актера по имени")
@allure.description("Поиск существующего актера по имени Дэвид Духовны")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.positive_test_api
@pytest.mark.test_api
def test_search_actor_by_name(api):
    name = "Дэвид Духовны"
    with allure.step("Отправить get-запрос с именем Дэвид Духовны на UTF-8"):
        url = f"{api.base_url}/api/v1/persons"
        headers = api.get_headers()
        params = {"name": name}
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        data = resp.json()
    with allure.step("проверка: в ответе код 200, nameRu='Дэвид Духовны"):
        assert resp.status_code == 200
        data = resp.json()
        assert 'items' in data
        assert isinstance(data['items'], list)
        assert len(data['items']) > 0
        first_item = data['items'][0]
        assert 'nameRu' in first_item
        assert first_item['nameRu'] == "Дэвид Духовны"


@allure.title("Поиск несуществующего актера по имени")
@allure.description("Поиск несуществующего актера по имени Джони Депович")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.negative_test_api
@pytest.mark.test_api
def test_search_nonexistent_actor_by_name(api):
    name = "Джони Депович"
    with allure.step("Отправить get-запрос 'Джони Депович' на UTF-8"):
        url = f"{api.base_url}/api/v1/persons"
        headers = api.get_headers()
        params = {"name": name}
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        data = resp.json()
    with allure.step("Проверка: в ответе  код 200, в теле total: 0"):
        assert resp.status_code == 200
        assert data["total"] == 0


@allure.title("Поиск актера по id актера")
@allure.description("Поиск существующего актера по его id")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.positive_test_api
@pytest.mark.test_api
def test_search_actor_by_id(api):
    actor_id = 41104
    with allure.step("Отправить get-запрос с id=41104"):
        url = f"{api.base_url}/api/v1/staff/{actor_id}"
        headers = api.get_headers()
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        data = resp.json()

    with allure.step("проверить, что ответ содержит код 200, personId = 41104"):
        assert resp.status_code == 200
        assert data["personId"] == actor_id


@allure.title("Поиск актера по несуществующему id")
@allure.description("Поиск актера по несуществующему id=9999999")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.negative_test_api
@pytest.mark.test_api
def test_search_actor_by_nonexistent_id(api):
    actor_id = 9999999
    with allure.step("Отправить get-запрос с id=9999999"):
        url = f"{api.base_url}/api/v1/staff/{actor_id}"
        headers = api.get_headers()
        resp = requests.get(url, headers=headers)
    with allure.step("проверить, что ответ содержит код 404"):
        assert resp.status_code == 404
