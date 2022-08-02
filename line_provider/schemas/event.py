import decimal
import enum
import random
from datetime import datetime, timedelta
from uuid import uuid4

from pydantic import UUID4, BaseModel, Field


def coefficient_factory() -> decimal.Decimal:
    return decimal.Decimal(random.randint(100, 200) / 100)


def deadline_factory() -> datetime:
    delta_in_seconds = timedelta(seconds=random.randint(10000, 20000))

    return datetime.now() + delta_in_seconds


class EventState(str, enum.Enum):
    PENDING = "PENDING"
    FIRST_COMMAND_WIN = "FIRST_COMMAND_WIN"
    FIRST_COMMAND_LOSE = "FIRST_COMMAND_LOSE"


class Event(BaseModel):
    event_id: UUID4 = Field(default_factory=uuid4)
    coefficient: decimal.Decimal = Field(default_factory=coefficient_factory)
    deadline: datetime = Field(default_factory=deadline_factory)
    state: EventState = Field(default=EventState.PENDING)
