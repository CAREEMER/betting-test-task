import decimal
import enum
from datetime import datetime

from pydantic import UUID4, BaseModel


class EventState(str, enum.Enum):
    PENDING = "PENDING"
    WIN = "WIN"
    LOSE = "LOSE"


class Event(BaseModel):
    """ For swagger typehinting. """

    event_id: UUID4
    coefficient: decimal.Decimal
    deadline: datetime
    state: EventState
