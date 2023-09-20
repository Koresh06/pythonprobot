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

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
