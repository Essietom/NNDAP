from farm_api.resources.cows_resource import COWS_ENDPOINT
from tests.integration.conf_test import client


NUM_COWS_IN_BASE_DB = 2


def test_cows_post(client):
    new_cow_json = {
    "name": "Camel",
    "sex": "female",
    "birthdate": "2023-03-07 11:50:22",
    "condition": "unhealthy",
    "weight": {
        "mass_kg": 101,
        "last_measured": "2023-03-07 11:50:22"
    },
    "feeding": {
        "amount_kg": 5,
        "cron_schedule": "*/3 * * * *",
        "last_measured": "2023-03-07 11:50:22"
    },
    "milk_production": {
        "last_milk": "2023-03-07 11:50:22",
        "cron_schedule": "*/3 * * * *",
        "amount_l": 10
    },
    "has_calves": True
}
    response = client.post(f"{COWS_ENDPOINT}", json=new_cow_json)
    assert response.status_code == 201


def test_cows_post_error(client):
    missing_cow_json = {"name": "Hopkins"}
    response = client.post(f"{COWS_ENDPOINT}", json=missing_cow_json)
    assert response.status_code == 400


def test_get_all_cows(client):
    response = client.get(f"{COWS_ENDPOINT}")
    assert response.status_code == 200
    assert len(response.json) == NUM_COWS_IN_BASE_DB


def test_get_all_cows_by_name(client):
    response = client.get(f"{COWS_ENDPOINT}?name=Japheth")

    for cow in response.json:
        assert cow["name"] == "Japheth"


def test_get_single_cow(client):
    response = client.get("/api/cow?cow_id=1")

    assert response.status_code == 200


def test_get_single_cow_not_found(client):
    response = client.get("/api/cow?id=16")
    assert response.status_code == 400