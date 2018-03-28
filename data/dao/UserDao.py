# -*- coding: utf-8 -*-
from AbstractDao import AbstractDao
from types import IntType
from data.entity.UserEntity import UserEntity


class UserDao(AbstractDao):
    @staticmethod
    def select_user_by_id(id):
        """
            Given a L{user_id}, selects the corresponding C{UserEntity}

            @type user_id: IntType
            @rtype: UserEntity
        """
        assert isinstance(id, IntType), type(id)

        return (UserDao.get_db_connection().query(UserEntity)
                .filter(UserEntity.id == id).one())

    @staticmethod
    def insert_user(user):
        """
            Adds L{user} to the database
        """
        assert isinstance(user, UserEntity), type(user)
        UserDao.get_db_connection().add(user)
