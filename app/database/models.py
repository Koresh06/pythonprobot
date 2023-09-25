from sqlalchemy import ForeignKey, String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from datetime import date
from typing import List, Optional
import config

engine = create_async_engine(
    url=config.SQLALCHEMY_URL,
    echo=config.SQLALCHEMY_ECHO
)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass

# Будущие модели

""" 
1. Юзеры (тг_ид, премиум бул)
2. Валюты (название и код)
3. Счета (какого юзера, название, валюта (2), баланс)
4. Категории (название, направление (пополнить/расход))
5. Направления (категория (4), название (зарплата или покупка продуктов))
6. Транзакции (дата, сумма, счёт (3), направление (5))
"""

class User(Base):
    
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    premium: Mapped[bool] = mapped_column(default=False)
    
class Currency(Base): #валюта
    
    __tablename__ = 'currencies'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(10))
    code: Mapped[str] = mapped_column(String(10))
    
class Score(Base): #счёт
    
    __tablename__ = 'score'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id_user: Mapped[int] = mapped_column()
    name: Mapped[str] = mapped_column(String(10))
    currency: Mapped[str] = mapped_column(String(10))
    balance: Mapped[float] = mapped_column()
    
class Categories(Base): #категория
    
    __tablename__ = 'categories'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(10))
    derection: Mapped[str] = mapped_column(String(10))
    
class Derection(Base): #направление
    
    __tablename__ = 'derection'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    categories: Mapped[str] = mapped_column(String(10))
    name: Mapped[str] = mapped_column(String(10))
    
class Transactions(Base): #транзакция
    
    __tablename__ = 'transactions'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[str] = mapped_column(date)   
    summ: Mapped[float] = mapped_column()
    currency: Mapped[str] = mapped_column(String(10))
    derection: Mapped[str] = mapped_column(String(10))


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
