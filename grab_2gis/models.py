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


class Item(Base, IdMixin):
    __tablename__ = 'stores'

    sqlite_autoincrement = True

    title    = Column(types.Unicode())
    kind     = Column(types.Unicode())
    lat      = Column(types.Float()) # координата: широта
    lon      = Column(types.Float()) # координата: долгота
    phones   = Column(types.Unicode())
    webinfo  = Column(types.Unicode())
    schedule = Column(types.Unicode())
    pay      = Column(types.Unicode())
