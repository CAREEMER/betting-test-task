from decimal import Decimal
from enum import Enum

from pydantic import UUID4, BaseModel, Field


class BetState(str, Enum):
    PENDING = "PENDING"
    WIN = "WIN"
    LOSE = "LOSE"


class BetCreate(BaseModel):
    event_id: UUID4
    amount: Decimal


class Bet(BetCreate):
    bet_id: UUID4
    state: BetState = Field(default=BetState.PENDING)
