from datetime import datetime

import uvicorn
from fastapi import FastAPI, HTTPException, Path
from pydantic import UUID4
from starlette import status

from db.memory import events
from schemas.event import Event, EventState
from services.bet_maker import BetMaker

app = FastAPI()


@app.post("/event")
async def create_event(event: Event):
    if event.event_id not in events:
        events[event.event_id] = event
        return {}

    return {}


@app.patch("/event/{event_id}")
async def patch_event(state: EventState, event_id: UUID4 = Path(default=None)):
    if not str(event_id) in events:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    events[str(event_id)].state = state.name

    await BetMaker.send_event_update(str(event_id), state.name)


@app.get("/event/{event_id}")
async def get_event(event_id: str = Path(default=None)):
    if event_id in events:
        return events[event_id]

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.get("/events")
async def get_events():
    return list(e for e in events.values() if datetime.now().timestamp() < e.deadline.timestamp())


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001)
