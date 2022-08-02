from uuid import uuid4

import aioredis
import orjson

from core.settings import app_settings
from schemas.bet import Bet, BetCreate


class RedisDB:
    def __init__(self):
        self.redis_conn = aioredis.from_url(app_settings.redis_dsn)
        self.key_prefix = "BET_MAKER"

    async def get_bet(self, key: str) -> Bet:
        return Bet.parse_raw(await self.redis_conn.get(key))

    async def save_bet(self, bet: Bet):
        await self.redis_conn.set(f"{self.key_prefix}:{bet.event_id}:{bet.bet_id}", bet.json())

    async def create_bet(self, bet: BetCreate):
        bet_data = bet.dict()
        bet_id = str(uuid4())
        bet_data["amount"] = str(bet_data["amount"])
        bet_data["bet_id"] = bet_id

        await self.redis_conn.set(
            f"{self.key_prefix}:{bet.event_id}:{bet_id}", orjson.dumps(bet_data, orjson.OPT_SERIALIZE_UUID)
        )

    async def list_bets(self):
        all_keys = await self.redis_conn.keys(self.key_prefix + "*")
        output = []

        for key in all_keys:
            output.append(Bet.parse_raw(await self.redis_conn.get(key)))

        return output

    async def update_bets(self, event_id: str, state: str):
        event_bets_keys = await self.redis_conn.keys(f"{self.key_prefix}:{event_id}:*")

        for key in event_bets_keys:
            bet = await self.get_bet(key)
            bet.state = state
            await self.save_bet(bet)


async def get_redis():
    return RedisDB()
