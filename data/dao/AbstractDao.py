# -*- coding: utf-8 -*-
from connectionmanager import manager


class AbstractDao(object):

    @staticmethod
    def get_db_connection():
        return manager.session

