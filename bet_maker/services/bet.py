from fastapi import Depends, HTTPException, Path
from pydantic import UUID4

from db.redis import RedisDB, get_redis
from schemas.bet import BetCreate, Prediction
from services.line_provider import LineProvider


class BetHandler:
    @staticmethod
    async def create_bet(bet: BetCreate, redis_db: RedisDB = Depends(get_redis)):
        possible_events = await LineProvider().get_events(only_available=True)
        if str(bet.event_id) not in [event.get("event_id") for event in possible_events]:
            raise HTTPException(status_code=404)

        await redis_db.create_bet(bet)

    @staticmethod
    async def update_bets(
        state: Prediction, event_id: UUID4 = Path(), redis_db: RedisDB = Depends(get_redis),
    ):
        await redis_db.update_bets(str(event_id), state)

    @staticmethod
    async def list_bets():
        return await RedisDB().list_bets()
