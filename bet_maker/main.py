from typing import List

import uvicorn
from fastapi import Depends, FastAPI, Response
from starlette import status

from db.redis import RedisDB, get_redis
from schemas.bet import Bet
from schemas.event import Event
from services.bet import BetHandler
from services.line_provider import LineProvider

app = FastAPI()


@app.get("/events", response_model=List[Event])
async def list_events() -> List[Event]:
    return await LineProvider().get_events()


@app.post("/bet")
async def create_bet(_=Depends(BetHandler.create_bet)):
    return Response(status_code=status.HTTP_201_CREATED)


@app.get("/bets", response_model=List[Bet])
async def list_bets(redis_db: RedisDB = Depends(get_redis)):
    # TODO: replace with service
    return await redis_db.list_bets()


@app.post("/update-bets/{event_id}/")
async def update_bets(_=Depends(BetHandler.update_bets)):
    """ Method for line_provider microservice to update bet entries related to the changed event. """

    return Response(status_code=status.HTTP_202_ACCEPTED)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
