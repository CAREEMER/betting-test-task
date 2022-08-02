import httpx
import random

from settings import app_settings


def get_events():
    events_list_url = "/events"
    response = httpx.get(app_settings.bet_maker_url + events_list_url)
    events = response.json()

    assert response.status_code == 200
    assert len(events) > 1

    return events


def bet_on_event(event_id: str):
    create_bet_url = "/bet"
    data = {
        "event_id": event_id,
        "amount": 100.51
    }

    response = httpx.post(app_settings.bet_maker_url + create_bet_url, json=data)

    assert response.status_code == 201


def get_bets():
    list_bets_url = "/bets"
    response = httpx.get(app_settings.bet_maker_url + list_bets_url)
    bets = response.json()

    assert response.status_code == 200
    assert len(bets) == 1

    return bets


def update_event_state(event_id: str):
    state = random.choice(["WIN", "LOSE"])
    change_event_url = f"/event/{event_id}?state={state}"

    response = httpx.patch(app_settings.line_provider_url + change_event_url)

    assert response.status_code == 200


def run_e2e_test():
    events = get_events()

    event = random.choice(events)
    bet_on_event(event["event_id"])
    get_bets()
    update_event_state(event["event_id"])
    updated_bet = get_bets()

    assert updated_bet[0]["state"] != "PENDING"


if __name__ == "__main__":
    run_e2e_test()
    print("E2E TEST COMPLETED")
