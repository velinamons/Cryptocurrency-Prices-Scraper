from pydantic import BaseModel, Field
from typing import Optional, List


class UserBase(BaseModel):
    telegram_id: str = Field(..., description="The Telegram ID of the user")
    name: Optional[str] = Field(None, description="Optional name of the user")


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int = Field(..., description="The unique ID of the user")
    subscriptions: Optional[List[int]] = Field(
        None, description="IDs of subscriptions for the user"
    )

    class Config:
        orm_mode = True


class CurrencyPairBase(BaseModel):
    pair: str = Field(..., description="The currency pair (e.g., BTCUSDT)")
    description: Optional[str] = Field(None, description="Optional description of the currency pair")


class CurrencyPairResponse(CurrencyPairBase):
    id: int = Field(..., description="The unique ID of the currency pair")

    class Config:
        orm_mode = True


class SubscriptionBase(BaseModel):
    currency_pair_id: int = Field(..., description="The ID of the currency pair being subscribed to")


class SubscriptionCreate(SubscriptionBase):
    user_id: int = Field(..., description="The ID of the user creating the subscription")


class SubscriptionResponse(SubscriptionBase):
    id: int = Field(..., description="The unique ID of the subscription")

    class Config:
        orm_mode = True
