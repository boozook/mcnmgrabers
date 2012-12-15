# -*- coding: utf-8 -*-
"""
Models for default project
"""
from datetime import datetime

from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, Integer, Text, String, ForeignKey,
                        DateTime, PickleType, Table)

from sqlalchemy import types

Base = declarative_base()

class IdMixin(object):
    """
    Provides the :attrs:`id` primary key column
    """
    id = Column(Integer(), primary_key=True) # уникальный идентификатор

class TimestampMixin(object):
    """Adds automatically updated created_at and updated_at timestamp
    columns to a table, that unsurprisingly are updated on record INSERT and
    UPDATE. UTC time is used in both cases.
    """

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False) # дата-время добавления записи
    updated_at = Column(DateTime, onupdate=datetime.utcnow, default=datetime.utcnow) # дата-время обновления записи


class Item(Base, IdMixin, TimestampMixin):
    __tablename__ = 'data'

    sqlite_autoincrement = True

    title = Column(types.Unicode(length=2000))
    times = Column(types.Unicode(length=2000))
    metro = Column(types.Unicode(length=2000))
    tel = Column(types.Unicode(length=2000))
    address = Column(types.Unicode(length=2000))
    tc = Column(types.Unicode(length=2000))
    tc_url = Column(types.Unicode(length=2000))
    city = Column(types.Unicode(length=2000))


