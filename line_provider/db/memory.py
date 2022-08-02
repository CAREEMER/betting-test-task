from schemas.event import Event

events = {}


def generate_mock_data():
    for _ in range(10):
        event = Event()
        events[str(event.event_id)] = event


generate_mock_data()
