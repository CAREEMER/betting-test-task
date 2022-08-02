from decimal import Decimal
from enum import Enum

from pydantic import UUID4, BaseModel, Field, condecimal


class BetResult(str, Enum):
    """ Enum that stores bet state (is it won, lost or pending). """

    PENDING = "PENDING"
    WIN = "WIN"
    LOSE = "LOSE"


class Prediction(str, Enum):
    FIRST_COMMAND_WIN = "FIRST_COMMAND_WIN"
    FIRST_COMMAND_LOSE = "FIRST_COMMAND_LOSE"


class BetCreate(BaseModel):
    event_id: UUID4
    amount: condecimal(gt=Decimal(0), decimal_places=2)
    prediction: Prediction


class Bet(BetCreate):
    bet_id: UUID4
    bet_result: BetResult = Field(default=BetResult.PENDING)
