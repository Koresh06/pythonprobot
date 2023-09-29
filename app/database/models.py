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
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id = mapped_column(BigInteger)
    premium: Mapped[bool] = mapped_column(default=False)
    
    account_rel: Mapped['Account'] = relationship(back_populates='user_rel', cascade='all, delete')
    
class Currency(Base): #валюта
    
    __tablename__ = 'currency'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(10))
    
    account_rel: Mapped['Account'] = relationship(back_populates='currency_rel', cascade='all, delete')
    
class Account(Base): #счёт
    
    __tablename__ = 'account'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[int] = mapped_column(ForeignKey('user.id', ondelete='CASCADE'))
    name: Mapped[str] = mapped_column(String(19))
    currency: Mapped[str] = mapped_column(ForeignKey('currency.id', ondelete='CASCADE'))
    balance: Mapped[float]
    
    user_rel: Mapped['User'] = relationship(back_populates='account_rel')
    currency_rel: Mapped['Currency'] = relationship(back_populates='account_rel')
    
    transactions_rel: Mapped['Transactions'] = relationship(back_populates='account_rel', cascade='all, delete')
    
class Categories(Base): #категория
    
    __tablename__ = 'categories'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(10))
    derection: Mapped[str] = mapped_column(String(10))
    
    derection_rel: Mapped['Derection'] = relationship(back_populates='categories_rel', cascade = 'all, delete')
    
class Derection(Base): #направление
    
    __tablename__ = 'derection'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    categories: Mapped[str] = mapped_column(ForeignKey('categories.name'), onupdate='CASCADE')
    name: Mapped[str] = mapped_column(String(10))
    
    categories_rel: Mapped['Categories'] = relationship(back_populates='derection_rel')
    transactions_rel: Mapped['Transactions'] = relationship(back_populates='derection_rel')
    
class Transactions(Base): #транзакция
    
    __tablename__ = 'transactions'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[str] = mapped_column(date)   
    summ: Mapped[float] = mapped_column()
    currency: Mapped[str] = mapped_column(ForeignKey('account.currency'), onupdate='CASCADE')
    derection: Mapped[str] = mapped_column(ForeignKey('derection.name'), onupdate='CASCADE')
    
    currency_rel: Mapped['Account'] = relationship(back_populates='transactions_rel')
    derection_rel: Mapped['Derection'] = relationship(back_populates='transactions_rel')


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
