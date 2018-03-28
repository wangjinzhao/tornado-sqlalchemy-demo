# -*- coding: utf-8 -*-
from data.entity.AbstractEntity import AbstractEntity
from sqlalchemy import Column, Integer, String, DateTime, Date, Boolean
import datetime
import json


class UserEntity(AbstractEntity):
    __tablename__ = 'user'
    __slots__ = (
        'id', 'user_name', 'accesskey', 'accesskey_secret',
        'created_time', 'deleted', 'enable', 'last_modified_time')

    id = Column(String(20), primary_key=True)
    user_name = Column(String(20))
    accesskey = Column(String(64))
    accesskey_secret = Column(String(64))
    created_time = Column(DateTime, nullable=False)
    deleted = Column(Boolean)
    enable = Column(Boolean)
    last_modified_time = Column(DateTime, nullable=False)

    def __init__(self, id, user_name, accesskey, accesskey_secret, created_time, deleted, enable, last_modified_time):
        self.id = id
        self.user_name = user_name
        self.accesskey = accesskey
        self.accesskey_secret = accesskey_secret
        self.created_time = created_time
        self.deleted = deleted
        self.enable = enable
        self.last_modified_time = last_modified_time
