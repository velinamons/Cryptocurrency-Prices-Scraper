from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=True)

    subscriptions = relationship("Subscription", back_populates="user")


class CurrencyPair(Base):
    __tablename__ = "currency_pairs"

    id = Column(Integer, primary_key=True, index=True)
    pair = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    currency_pair_id = Column(Integer, ForeignKey("currency_pairs.id"), nullable=False)

    user = relationship("User", back_populates="subscriptions")
